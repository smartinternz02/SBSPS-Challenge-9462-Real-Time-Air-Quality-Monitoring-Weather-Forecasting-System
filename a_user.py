try:
    import usocket as socket

except:
    import socket

from machine import Pin

import network

from umqttsimple import MQTTClient
import esp
esp.osdebug(None)
import gc

gc.collect()

ssid = 'Kush'

password = '12345678'

SERVER = "mqtt.thingspeak.com"

client = MQTTClient("umqtt_client", SERVER)

CHANNEL_ID = "432115"
WRITE_API_KEY = "T1YZO2FMPOBOL6C5"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
