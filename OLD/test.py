from collections import namedtuple
import yaml

f = open('tunnel.yaml')
# use safe_load instead load
obj = yaml.safe_load(f)
f.close()

print obj

dict = {'foo': 'bar'}

print dict['foo']
dict.get('foo', 'default')

Config = namedtuple('Config', 'url, user, pw')

Config.url = "foo"
Config.user = 'ivo'
Config.pw = None
Config.foo = "abc"

print Config.url
print Config.user
print Config.pw
print Config.foo



