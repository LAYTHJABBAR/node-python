from decimal import Decimal
import time
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import math
import RPi.GPIO as GPIO

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



def subscribeFunction(self, param, packet):
    relayPin = 18 #define relay pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(relayPin,GPIO.OUT)
    print("New message Recieved: "+packet.topic)
    print(packet.payload)
    GPIO.output(relayPin,GPIO.HIGH) #Starting relay
    print("turn on")
    time.sleep(1)
    GPIO.output(relayPin,GPIO.LOW) #Close relay
    print("turn off")
    time.sleep(1)
    GPIO.cleanup()


myAWSIoTMQTTClient.connect()
def loop():
    while True:
        time.sleep(2)
        myAWSIoTMQTTClient.subscribe(
         "RealTimeDataTransfer/startmotor",
         1,
         subscribeFunction)
        time.sleep(18)
 
try:
 
    loop()
except KeyboardInterrupt:
    pass