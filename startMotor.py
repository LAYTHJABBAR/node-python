from asyncio import sleep
from decimal import Decimal
import RPi.GPIO as GPIO
import time
import smbus
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import math



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
   

relayPin = 18 #define relay pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relayPin,GPIO.OUT)

 
def subscribeFunction(self, param, packet):
    print("New message Recieved: "+packet.topic)
    print(packet.payload)
    # while True:
    #  GPIO.output(relayPin,GPIO.HIGH) #Starting relay
    #  print("turn on")
    #  sleep(2)
    #  GPIO.output(relayPin,GPIO.LOW) #Close relay
    #  print("turn off")
    #  sleep(1)
    #  GPIO.cleanup()
 

myAWSIoTMQTTClient.connect()
def loop():
    while True:
        myAWSIoTMQTTClient.subscribe(
         "RealTimeDataTransfer/humid",
         1,
         subscribeFunction)
        time.sleep(900)
   
        
try:
    loop()
except KeyboardInterrupt:
    pass