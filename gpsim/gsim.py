import sys,os
import time
import threading
import serial
import re
import datetime

# $GPGGA,194950.000,3253.5959,N,11711.7638,W,1,10,1.1,77.5,M,-35.6,M,,0000*5D
# $GPGGA,135023.000,3253.5959,N,11711.7638,W,1,8,1.1,58.2,M,-35.6,M,,0000*68
# $GPRMC,194948.000,A,3253.5836,N,11711.7921,W,46.96,65.60,300517,,,A*78
# $GPRMC,135023.000,A,3253.5959,N,11711.7638,W,46.96,65.60,090617,,,A*71

'''
(No. of Satellites from GGA sentence >= 4)
AND (HDOP from GGA sentence <= 10)
AND (Quality parameter from GGA should indicate that fix is valid)'''

def number_format_for_GPRMC(number):
    if number < 0 or number > 999.9:
        print("The knotrate must be more than 0 and less than 999.9")
        os.exit()
    else:
        if number>=100:
            number = "%.1f"%number
        else:
            integer = int(number)
            decimal = number - integer
            number = ("%02d"%integer)+("%.2f"%decimal)[1:]
    return number

def number_format_for_GPVTG(number):
    if number < 0 or number > 999.9:
        print("The knotrate must be betweent 0 and 999.9")
        os.exit()
    else:
        if number>=100:
            number = "%.2f"%number
        else:
            integer = int(number)
            decimal = number - integer
            number = ("%02d"%integer)+("%.3f"%decimal)[1:]
    return number

def modifys_speedrate(gpsline,knotrate):
    gpsline = gpsline.split(',')
    if gpsline[0] == "$GPRMC":
        knotrate = number_format_for_GPRMC(knotrate)
        gpsline[7] = knotrate
    elif gpsline[0] == "$GPVTG":
        knotrate = number_format_for_GPVTG(knotrate)
        gpsline[5] = knotrate
    return ','.join(gpsline)

def modify_satelitesnumber(gpsline,satelitesnumber):
    if satelitesnumber < 0 or satelitesnumber > 12:
        print("error! The satelites number must be betweent 0 and 12")
        os._exit(0)
    gpsline = gpsline.split(',')
    satelitesnumber = "%02d"%satelitesnumber
    if gpsline[0] == "$GPGGA":
        gpsline[7] = satelitesnumber
    return ','.join(gpsline)

def modify_HDOP(gpsline,HDOP):
    if HDOP < 0.5 or HDOP > 99.9:
        print("error! The HDOP must be betweent 0.5 and 99.9")
        os._exit(0)
    gpsline = gpsline.split(',')
    if gpsline[0] == "$GPGGA":
        gpsline[8] = str(HDOP)
    return ','.join(gpsline)

def modify_GGAquality(gpsline,GGAquality):
    if GGAquality in (0,1,2,6):
        gpsline = gpsline.split(',')
        if gpsline[0] == "$GPGGA":
            gpsline[6] = str(GGAquality)
        return ','.join(gpsline)
    else:
        print("error! The HDOP must be 0,1,2,6")
        os._exit(0)

def modify_timeanddate(gpsline):
    szTime = "%s%s%s.000" % (time.strftime("%H"), time.strftime("%M"), time.strftime("%S"))
    # szTime = bytes(szTime, 'utf8')
    szDate = "%s%s%s" % (time.strftime("%d"), time.strftime("%m"), time.strftime("%y"))
    # szDate = bytes(szDate, 'utf8')

    utc = datetime.datetime.utcnow()
    utcTime = "%s%s%s.000" % (utc.strftime("%H"), utc.strftime("%M"), utc.strftime("%S"))
    # utcTime = bytes(szTime, 'utf8')
    utcDate = "%s%s%s" % (utc.strftime("%d"), utc.strftime("%m"), utc.strftime("%y"))
    # utcDate = bytes(szDate, 'utf8')
	
    gpsline = gpsline.split(',')
    if gpsline[0] == "$GPGGA":
        # gpsline[1] = szTime
        gpsline[1] = utcTime
    if gpsline[0] == "$GPRMC":
        # gpsline[1] = szTime
        # gpsline[9] = szDate
        gpsline[1] = utcTime
        gpsline[9] = utcDate
    return ','.join(gpsline)

def nmeasum(gpsline):
    checksum = 0
    i = 1
    nMessageLen = len(gpsline) - 1

    while True:
        if i >= nMessageLen:
            break
        else:
            checksum = (checksum ^ gpsline[i])
        i = i + 1

        if i > 250:
            return 0

    return b"%02X" % checksum

class GPSsimulator:

    def __init__(self, port, file_name):
        self.serial = serial.Serial()
        self.serial.port = port
        self.serial.timeout = 5
        self.serial.baudrate = 4800
        self.serial.writeTimeout = 0
        self.is_open = self.open()
        self.running = True
        self.Thsendgps = threading.Thread(target=self.send_gps,args=(file_name,))
        self.Thsendgps.setDaemon(True)
        self.Thsendgps.start()

    def open(self):

        ret = False
        try:
            print(self.serial)
            self.serial.open()

        except serial.SerialException as e:
            print(sys.exc_info(), e.__cause__)
        else:
            ret = True

        return ret


    def close(self):
        if self.serial.isOpen():
            self.serial.close()
            # print('serial close')

    def send_gps(self, filename):
        linenumber = 1
        print('gps thread started')
        f = open(filename, 'r')
        try:
            while self.running:
                for line in f.readlines():
                    line = modify_timeanddate(line)
                    # line = "%s\r\n" % line[:-1]
                    # line = bytes(line, encoding='utf8')
                    line = bytes(line,encoding='utf8')[:-3]
                    gpssum = nmeasum(line)
                    Msg = line + gpssum + b'\r\n'
                    print("%d\t%s" % (linenumber, Msg))
                    self.serial.write(Msg)
                    if linenumber%2 == 0:
                        # self.serial.flushOutput()
                        # self.serial.flushInput()
                        print("wait 0.998 second")
                        time.sleep(0.998)
                    else:
                        print("wait 0.001 second")
                        time.sleep(0.001)
                    linenumber += 1
        except serial.SerialException as e:
            self.running = False
            print('SerialException:' + str(e))
            # self.terminal.cancel()
        finally:
            print("gps thread quit")


if __name__ == "__main__":
    sb = GPSsimulator('/dev/ttyUSB0', "raw nmea miramar road modified w new rules non stationary.nmea")
    # sb = GPSsimulator('COM10', "raw nmea 56w gpgga gprmc w rules.nmea")
    while True:
        time.sleep(1)

