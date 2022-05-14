from decimal import Decimal
import RPi.GPIO as GPIO
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import smbus

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

# buz = 18
# GPIO.setup(buz,GPIO.OUT)

# address = 0x48 ##address--->device address
# cmd = 0x40
# A0 = 0x40    ##A0---->port address
# A1 = 0x41
# A2 = 0x42
# A3 = 0x43
# bus = smbus.SMBus(1) 

def helloworld(self, params, packet):
    print('received message from AWS IOT Core')
    print('Topic:' + packet.topic)
    print('payload:'+ packet.payload)

# def analogRead(count):   #function,read analog data
#     read_val = bus.read_byte_data(address,cmd+count)
#     return read_val;

myMQTTClient = AWSIoTMQTTClient("RishabClientID") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("a1l83aslu1wtwg-ats.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/pi/AWSIoT/AmazonRootCA1.pem", "/home/pi/AWSIoT/private.pem.key", "/home/pi/AWSIoT/certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()

myMQTTClient.susbscribe("home/helloworld", 1, helloworld)

while True:
    time.sleep(5)

# def loop():
#     while True:
#         analogVal = analogRead(0) 
#         Vr = 5 * float(analogVal) / 255
#         Rt = 10000 * Vr / (5 - Vr)
#         temperature = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))
#         temperature = (temperature - 273.15)
#         temperature = round(temperature, 1)
#         fahrenheit = ((temperature*1.8)+32)
#         time.sleep(.5)
#         print("Sending Temperature: ", fahrenheit)


#         myMQTTClient.publish(
#             topic="RealTimeDataTrasfer/Temperature",
#             QoS=1,
#             payload='{"Temperature":"'+str(fahrenheit)+'"}')


# try:
#     loop()
# except KeyboardInterrupt:
#     pass