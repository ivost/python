import time
import datetime

import struct
import paho.mqtt.client as mqtt

from random import seed, randint

from bluepy.btle import UUID, Peripheral, ADDR_TYPE_RANDOM, DefaultDelegate
import argparse
import time
#import struct
import binascii

# MQTT

def mqtt_init():
    global mqtt_client
    mqtt_client = mqtt.Client("ivo-thingy52")
    mqtt_client.connect("test.mosquitto.org", 1883)

def publish(typ, val):
    print('PUBLISH - type:  {}, value: {}'.format(typ, val))
    mqtt_client.publish(typ, val)  # Publish message to MQTT broker

def write_uint16(data, value, index):
    """ Write 16bit value into data string at index and return new string """
    data = data.decode('utf-8')  # This line is added to make sure both Python 2 and 3 works
    return '{}{:02x}{:02x}{}'.format(
                data[:index*4],
                value & 0xFF, value >> 8,
                data[index*4 + 4:])

def write_uint8(data, value, index):
    """ Write 8bit value into data string at index and return new string """
    data = data.decode('utf-8')  # This line is added to make sure both Python 2 and 3 works
    return '{}{:02x}{}'.format(
                data[:index*2],
                value,
                data[index*2 + 2:])

# Please see # Ref https://nordicsemiconductor.github.io/Nordic-Thingy52-FW/documentation
# for more information on the UUIDs of the Services and Characteristics that are being used
def Nordic_UUID(val):
    """ Adds base UUID and inserts value to return Nordic UUID """
    return UUID("EF68%04X-9B35-4933-9B10-52FFA9740042" % val)

# Definition of all UUID used by Thingy
CCCD_UUID = 0x2902

BATTERY_SERVICE_UUID = 0x180F
BATTERY_LEVEL_UUID = 0x2A19

ENVIRONMENT_SERVICE_UUID = 0x0200
E_TEMPERATURE_CHAR_UUID = 0x0201
E_PRESSURE_CHAR_UUID    = 0x0202
E_HUMIDITY_CHAR_UUID    = 0x0203
E_GAS_CHAR_UUID         = 0x0204
E_COLOR_CHAR_UUID       = 0x0205
E_CONFIG_CHAR_UUID      = 0x0206

USER_INTERFACE_SERVICE_UUID = 0x0300
UI_LED_CHAR_UUID            = 0x0301
UI_BUTTON_CHAR_UUID         = 0x0302
UI_EXT_PIN_CHAR_UUID        = 0x0303

# Notification handles used in notification delegate
e_temperature_handle = None
e_pressure_handle = None
e_humidity_handle = None
e_gas_handle = None
e_color_handle = None
ui_button_handle = None
m_tap_handle = None

class BatterySensor():
    """
    Battery Service module. Instance the class and enable to get access to Battery interface.
    """
    svcUUID = UUID(BATTERY_SERVICE_UUID)  # Ref https://www.bluetooth.com/specifications/gatt/services
    dataUUID = UUID(BATTERY_LEVEL_UUID) # Ref https://www.bluetooth.com/specifications/gatt/characteristics

    def __init__(self, periph):
        self.periph = periph
        self.service = None
        self.data = None

    def enable(self):
        """ Enables the class by finding the service and its characteristics. """
        if self.service is None:
            self.service = self.periph.getServiceByUUID(self.svcUUID)
        if self.data is None:
            self.data = self.service.getCharacteristics(self.dataUUID)[0]

    def read(self):
        """ Returns the battery level in percent """
        val = ord(self.data.read())
        return val


class EnvironmentService():
    """
    Environment service module. Instance the class and enable to get access to the Environment interface.
    """
    serviceUUID =           Nordic_UUID(ENVIRONMENT_SERVICE_UUID)
    temperature_char_uuid = Nordic_UUID(E_TEMPERATURE_CHAR_UUID)
    pressure_char_uuid =    Nordic_UUID(E_PRESSURE_CHAR_UUID)
    humidity_char_uuid =    Nordic_UUID(E_HUMIDITY_CHAR_UUID)
    gas_char_uuid =         Nordic_UUID(E_GAS_CHAR_UUID)
    color_char_uuid =       Nordic_UUID(E_COLOR_CHAR_UUID)
    config_char_uuid =      Nordic_UUID(E_CONFIG_CHAR_UUID)

    def __init__(self, periph):
        self.periph = periph
        self.environment_service = None
        self.temperature_char = None
        self.temperature_cccd = None
        self.pressure_char = None
        self.pressure_cccd = None
        self.humidity_char = None
        self.humidity_cccd = None
        self.gas_char = None
        self.gas_cccd = None
        self.color_char = None
        self.color_cccd = None
        self.config_char = None

    def enable(self):
        """ Enables the class by finding the service and its characteristics. """
        global e_temperature_handle
        global e_pressure_handle
        global e_humidity_handle
        global e_gas_handle
        global e_color_handle

        if self.environment_service is None:
            self.environment_service = self.periph.getServiceByUUID(self.serviceUUID)
        if self.temperature_char is None:
            self.temperature_char = self.environment_service.getCharacteristics(self.temperature_char_uuid)[0]
            e_temperature_handle = self.temperature_char.getHandle()
            self.temperature_cccd = self.temperature_char.getDescriptors(forUUID=CCCD_UUID)[0]
        if self.pressure_char is None:
            self.pressure_char = self.environment_service.getCharacteristics(self.pressure_char_uuid)[0]
            e_pressure_handle = self.pressure_char.getHandle()
            self.pressure_cccd = self.pressure_char.getDescriptors(forUUID=CCCD_UUID)[0]
        if self.humidity_char is None:
            self.humidity_char = self.environment_service.getCharacteristics(self.humidity_char_uuid)[0]
            e_humidity_handle = self.humidity_char.getHandle()
            self.humidity_cccd = self.humidity_char.getDescriptors(forUUID=CCCD_UUID)[0]
        if self.gas_char is None:
            self.gas_char = self.environment_service.getCharacteristics(self.gas_char_uuid)[0]
            e_gas_handle = self.gas_char.getHandle()
            self.gas_cccd = self.gas_char.getDescriptors(forUUID=CCCD_UUID)[0]
        if self.color_char is None:
            self.color_char = self.environment_service.getCharacteristics(self.color_char_uuid)[0]
            e_color_handle = self.color_char.getHandle()
            self.color_cccd = self.color_char.getDescriptors(forUUID=CCCD_UUID)[0]
        if self.config_char is None:
            self.config_char = self.environment_service.getCharacteristics(self.config_char_uuid)[0]

    def set_temperature_notification(self, state):
        if self.temperature_cccd is not None:
            if state == True:
                self.temperature_cccd.write(b"\x01\x00", True)
            else:
                self.temperature_cccd.write(b"\x00\x00", True)

    def set_pressure_notification(self, state):
        if self.pressure_cccd is not None:
            if state == True:
                self.pressure_cccd.write(b"\x01\x00", True)
            else:
                self.pressure_cccd.write(b"\x00\x00", True)

    def set_humidity_notification(self, state):
        if self.humidity_cccd is not None:
            if state == True:
                self.humidity_cccd.write(b"\x01\x00", True)
            else:
                self.humidity_cccd.write(b"\x00\x00", True)

    def set_gas_notification(self, state):
        if self.gas_cccd is not None:
            if state == True:
                self.gas_cccd.write(b"\x01\x00", True)
            else:
                self.gas_cccd.write(b"\x00\x00", True)

    def set_color_notification(self, state):
        if self.color_cccd is not None:
            if state == True:
                self.color_cccd.write(b"\x01\x00", True)
            else:
                self.color_cccd.write(b"\x00\x00", True)

    def configure(self, temp_int=None, press_int=None, humid_int=None, gas_mode_int=None,
                        color_int=None, color_sens_calib=None):
        if temp_int is not None and self.config_char is not None:
            current_config = binascii.b2a_hex(self.config_char.read())
            new_config = write_uint16(current_config, temp_int, 0)
            self.config_char.write(binascii.a2b_hex(new_config), True)
        if press_int is not None and self.config_char is not None:
            current_config = binascii.b2a_hex(self.config_char.read())
            new_config = write_uint16(current_config, press_int, 1)
            self.config_char.write(binascii.a2b_hex(new_config), True)
        if humid_int is not None and self.config_char is not None:
            current_config = binascii.b2a_hex(self.config_char.read())
            new_config = write_uint16(current_config, humid_int, 2)
            self.config_char.write(binascii.a2b_hex(new_config), True)
        if gas_mode_int is not None and self.config_char is not None:
            current_config = binascii.b2a_hex(self.config_char.read())
            new_config = write_uint8(current_config, gas_mode_int, 8)
            self.config_char.write(binascii.a2b_hex(new_config), True)
        if color_int is not None and self.config_char is not None:
            current_config = binascii.b2a_hex(self.config_char.read())
            new_config = write_uint16(current_config, color_int, 3)
            self.config_char.write(binascii.a2b_hex(new_config), True)
        if color_sens_calib is not None and self.config_char is not None:
            current_config = binascii.b2a_hex(self.config_char.read())
            new_config = write_uint8(current_config, color_sens_calib[0], 9)
            new_config = write_uint8(current_config, color_sens_calib[1], 10)
            new_config = write_uint8(current_config, color_sens_calib[2], 11)
            self.config_char.write(binascii.a2b_hex(new_config), True)

    def disable(self):
        set_temperature_notification(False)
        set_pressure_notification(False)
        set_humidity_notification(False)
        set_gas_notification(False)
        set_color_notification(False)

class UserInterfaceService():
    """
    User interface service module. Instance the class and enable to get access to the UI interface.
    """
    serviceUUID = Nordic_UUID(USER_INTERFACE_SERVICE_UUID)
    led_char_uuid = Nordic_UUID(UI_LED_CHAR_UUID)
    btn_char_uuid = Nordic_UUID(UI_BUTTON_CHAR_UUID)
    # To be added: EXT PIN CHAR

    def __init__(self, periph):
        self.periph = periph
        self.ui_service = None
        self.led_char = None
        self.btn_char = None
        self.btn_char_cccd = None
        # To be added: EXT PIN CHAR

    def enable(self):
        """ Enables the class by finding the service and its characteristics. """
        global ui_button_handle

        if self.ui_service is None:
            self.ui_service = self.periph.getServiceByUUID(self.serviceUUID)
        if self.led_char is None:
            self.led_char = self.ui_service.getCharacteristics(self.led_char_uuid)[0]
        if self.btn_char is None:
            self.btn_char = self.ui_service.getCharacteristics(self.btn_char_uuid)[0]
            ui_button_handle = self.btn_char.getHandle()
            self.btn_char_cccd = self.btn_char.getDescriptors(forUUID=CCCD_UUID)[0]

    def set_led_mode_off(self):
        self.led_char.write(b"\x00", True)

    def set_led_mode_constant(self, r, g, b):
        teptep = "01{:02X}{:02X}{:02X}".format(r, g, b)
        self.led_char.write(binascii.a2b_hex(teptep), True)

    def set_led_mode_breathe(self, color, intensity, delay):
        """
        Set LED to breathe mode.
        color has to be within 0x01 and 0x07
        intensity [%] has to be within 1-100
        delay [ms] has to be within 1 ms - 10 s
        """
        teptep = "02{:02X}{:02X}{:02X}{:02X}".format(color, intensity,
                delay & 0xFF, delay >> 8)
        self.led_char.write(binascii.a2b_hex(teptep), True)

    def set_led_mode_one_shot(self, color, intensity):
        """
        Set LED to one shot mode.
        color has to be within 0x01 and 0x07
        intensity [%] has to be within 1-100
        """
        teptep = "03{:02X}{:02X}".format(color, intensity)
        self.led_char.write(binascii.a2b_hex(teptep), True)

    def set_btn_notification(self, state):
        if self.btn_char_cccd is not None:
            if state == True:
                self.btn_char_cccd.write(b"\x01\x00", True)
            else:
                self.btn_char_cccd.write(b"\x00\x00", True)

    #def disable(self):
        # set_btn_notification(False)

class MyDelegate(DefaultDelegate):

    def handleNotification(self, hnd, data):
        #Debug print repr(data)
        if (hnd == e_temperature_handle):
            teptep = binascii.b2a_hex(data)
            v = 100*self._str_to_int(teptep[:-2]) + int(teptep[-2:], 16)
            print('Notification: Temp received:  {} degCelcius'.format(v))
            publish('tc', v)

        elif (hnd == e_pressure_handle):
            press_int, press_dec = self._extract_pressure_data(data)
            v = 100*press_int + press_dec
            print('Notification: Press received: {} hPa'.format(v))
            publish('ph', v)

        elif (hnd == e_humidity_handle):
            teptep = binascii.b2a_hex(data)
            v = self._str_to_int(teptep)
            print('Notification: Humidity received: {} %'.format(v))
            publish('hp', v)

        elif (hnd == e_gas_handle):
            eco2, tvoc = self._extract_gas_data(data)
            print('Notification: Gas received: eCO2 ppm: {}, TVOC ppb: {} %'.format(eco2, tvoc))

        elif (hnd == e_color_handle):
            teptep = binascii.b2a_hex(data)
            print('Notification: Color: {}'.format(teptep))

        elif (hnd == ui_button_handle):
            teptep = binascii.b2a_hex(data)
            print('Notification: Button state [1 -> released]: {}'.format(self._str_to_int(teptep)))

        elif (hnd == m_tap_handle):
            direction, count = self._extract_tap_data(data)
            print('Notification: Tap: direction: {}, count: {}'.format(direction, self._str_to_int(count)))
        else:
            teptep = binascii.b2a_hex(data)
            print('Notification: UNKOWN: hnd {}, data {}'.format(hnd, teptep))


    def _str_to_int(self, s):
        """ Transform hex str into int. """
        i = int(s, 16)
        if i >= 2**7:
            i -= 2**8
        return i

    def _extract_pressure_data(self, data):
        """ Extract pressure data from data string. """
        teptep = binascii.b2a_hex(data)
        pressure_int = 0
        for i in range(0, 4):
                pressure_int += (int(teptep[i*2:(i*2)+2], 16) << 8*i)
        pressure_dec = int(teptep[-2:], 16)
        return (pressure_int, pressure_dec)

    def _extract_gas_data(self, data):
        """ Extract gas data from data string. """
        teptep = binascii.b2a_hex(data)
        eco2 = int(teptep[:2]) + (int(teptep[2:4]) << 8)
        tvoc = int(teptep[4:6]) + (int(teptep[6:8]) << 8)
        return eco2, tvoc

    def _extract_tap_data(self, data):
        """ Extract tap data from data string. """
        teptep = binascii.b2a_hex(data)
        direction = teptep[0:2]
        count = teptep[2:4]
        return (direction, count)


class Thingy52(Peripheral):
    """
    Thingy:52 module. Instance the class and enable to get access to the Thingy:52 Sensors.
    The addr of your device has to be know, or can be found by using the hcitool command line
    tool, for example. Call "> sudo hcitool lescan" and your Thingy's address should show up.
    """
    def __init__(self, addr):
        Peripheral.__init__(self, addr, addrType=ADDR_TYPE_RANDOM)

        # Thingy configuration service not implemented
        self.battery = BatterySensor(self)
        self.environment = EnvironmentService(self)
        self.ui = UserInterfaceService(self)

def main():
    parser = argparse.ArgumentParser()

    #parser.add_argument('mac_address', action='store', help='MAC address of BLE peripheral')

    parser.add_argument('-n', action='store', dest='count', default=0,
                            type=int, help="Number of times to loop data")
    parser.add_argument('-t',action='store',type=float, default=10.0, help='time between polling')
    parser.add_argument('--temperature', action="store_true",default=True)
    parser.add_argument('--pressure', action="store_true",default=True)
    parser.add_argument('--humidity', action="store_true",default=True)
    parser.add_argument('--gas', action="store_true",default=False)
    parser.add_argument('--color', action="store_true",default=False)
    args = parser.parse_args()

    args.mac_address = 'cc:c0:16:27:8b:ca'

    print('Connecting to ' + args.mac_address)
    thingy = Thingy52(args.mac_address)
    print('Connected...')
    thingy.setDelegate(MyDelegate())
    interval = 30000
    mqtt_init()
    try:
        # Set LED so that we know we are connected
        thingy.ui.enable()
        thingy.ui.set_led_mode_breathe(0x01, 50, 100) # 0x01 = RED
        print('LED set to breathe mode...')

        # Enabling selected sensors
        print('Enabling selected sensors...')
        # Environment Service
        if args.temperature:
            thingy.environment.enable()
            thingy.environment.configure(temp_int=interval)
            thingy.environment.set_temperature_notification(True)
        if args.pressure:
            thingy.environment.enable()
            thingy.environment.configure(press_int=interval)
            thingy.environment.set_pressure_notification(True)
        if args.humidity:
            thingy.environment.enable()
            thingy.environment.configure(humid_int=interval)
            thingy.environment.set_humidity_notification(True)
        if args.gas:
            thingy.environment.enable()
            thingy.environment.configure(gas_mode_int=20)
            thingy.environment.set_gas_notification(True)
        if args.color:
            thingy.environment.enable()
            thingy.environment.configure(color_int=1000)
            thingy.environment.configure(color_sens_calib=[0,0,0])
            thingy.environment.set_color_notification(True)
        # User Interface Service
        thingy.ui.enable()
        #thingy.ui.set_btn_notification(True)
        thingy.battery.enable()

        # Allow sensors time to start up (might need more time for some sensors to be ready)
        print('All requested sensors and notifications are enabled...')
        time.sleep(1.0)

        while True:
            #print("Battery: ", thingy.battery.read())
            thingy.waitForNotifications(args.t)

    finally:
        print("Disconnecting")
        thingy.disconnect()
        del thingy


if __name__ == "__main__":
    main()