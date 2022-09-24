from machine import Pin
from time import sleep
import dht,math,time,network,micropython,esp
from machine import ADC
from umqttsimple import MQTTClient
import ubinascii
from MQ135 import MQ135


#sensor_dht = dht.DHT22(Pin(14))
sensor_dht = dht.DHT11(Pin(5))
sensor_mq135 = MQ135(0)

from umqttsimple import MQTTClient
SERVER = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", SERVER)

CHANNEL_ID = "432115"
WRITE_API_KEY = "T1YZO2FMPOBOL6C5"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
#Temperature, Humidity = collectData()
while True:
    sensor_dht.measure()
    temperature = sensor_dht.temperature()
    humidity = sensor_dht.humidity()
    
    rzero = sensor_mq135.get_rzero()
    corrected_rzero = sensor_mq135.get_corrected_rzero(temperature, humidity)
    resistance = sensor_mq135.get_resistance()
    ppm = sensor_mq135.get_ppm()
    corrected_ppm = sensor_mq135.get_corrected_ppm(temperature, humidity)

    payload = "field1="+str(temperature)+"&field2="+str(humidity)+"&field3="+str(corrected_ppm)

    client.connect()
    client.publish(topic, payload)
    print("Payload published successfully")
    #print(publish_check)
    client.disconnect() 
    time.sleep(30)
