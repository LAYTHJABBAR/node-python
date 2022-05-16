from decimal import Decimal
import RPi.GPIO as GPIO
import time
import smbus
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import math

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

buz = 18
GPIO.setup(buz,GPIO.OUT)

address = 0x48 ##address--->device address
cmd = 0x40
A0 = 0x40    ##A0---->port address
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1) 

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
ENDPOINT = "abw3iixgawgvv-ats.iot.us-west-2.amazonaws.com"
CLIENT_ID = "testDevice"
PATH_TO_CERTIFICATE = "/home/pi/AWSIoT/certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "/home/pi/AWSIoT/private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "/home/pi/AWSIoT/root-ca.pem"
MESSAGE = "Hello World"
TOPIC = "test/testing"
RANGE = 20

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

def analogRead(count):   #function,read analog data
    read_val = bus.read_byte_data(address,cmd+count)
    return read_val;
def subscribeFunction(self, param, packet):
    print("New message Recieved: "+packet.topic)
    print(packet.payload)
 

myAWSIoTMQTTClient.connect()
def loop():
    while True:
        myAWSIoTMQTTClient.subscribe(
         "RealTimeDataTransfer/humid",
         1,
         subscribeFunction)
        analogVal = analogRead(0)
        time.sleep(3600)
        myAWSIoTMQTTClient.publish(
            topic="RealTimeDataTransfer/humid",
            QoS=1,
            payload='{"humidity":"'+str(analogVal)+'","time":"'+str(time.time())+'"}')
        
        # analogVal = analogRead(0) 
        # Vr = 5 * float(analogVal) / 255
        # Rt = 10000 * Vr / (5 - Vr)
        # temperature = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))
        # temperature = (temperature - 273.15)
        # temperature = round(temperature, 1)
        # fahrenheit = ((temperature*1.8)+32)
        # time.sleep(.5)
        # print("Sending Temperature: ", fahrenheit)


        # myAWSIoTMQTTClient.publish(
        #     topic="RealTimeDataTrasfer/Temperature",
        #     QoS=1,
        #     payload='{"Temperature":"'+str(fahrenheit)+'"}')
try:
    loop()
except KeyboardInterrupt:
    pass