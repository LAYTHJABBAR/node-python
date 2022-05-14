import RPi.GPIO as GPIO
import time
import smbus
import paho.mqtt.client as mqtt

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

 

client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)
def analogRead(count):   #function,read analog data
    read_val = bus.read_byte_data(address,cmd+count)
    return read_val

while True:
    temp = analogRead(0)   ##read A0 data
    if(temp>20):
        GPIO.output(buz,GPIO.HIGH)
    else:
        GPIO.output(buz,GPIO.LOW)
        
    print("Temp = %s"%(temp) + 'C')    ##print data
    client.publish('raspberry/temp', payload= temp, qos=0, retain=False)
    print(f"send {temp} to raspberry/temp")
    time.sleep(1)
  
client.loop_forever()

GPIO.cleanup()