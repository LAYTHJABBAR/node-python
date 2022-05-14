import RPi.GPIO as GPIO
import time
import sys

     
GPIO.cleanup()  
status = int(sys.argv[1])
time.sleep(5)
ledPin = 18  #define led pin
ledPin2 = 17 #define buzzer pin
GPIO.setmode(GPIO.BCM)        # use BCM numbers
GPIO.setup(ledPin,GPIO.OUT)   #set the ledPin OUTPUT mode
GPIO.output(ledPin,GPIO.LOW)  # make ledPin output LOW level
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.output(ledPin2, GPIO.LOW)

if status == 1:
    while True:
        print(1)
        GPIO.output(ledPin,GPIO.HIGH) #turn OFF LED
        GPIO.output(ledPin2,GPIO.HIGH)  #turn on buzzer
    

if status == 0:
    while True:
        print(0)
        GPIO.output(ledPin,GPIO.LOW) #turn OFF LED
        GPIO.output(ledPin2,GPIO.LOW)  #turn on buzzer
    
 


  #release all GPIO