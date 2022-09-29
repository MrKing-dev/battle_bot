import RPi.GPIO as GPIO
from time import sleep
import gamepad_constants as gp
from evdev import InputDevice, categorize, ecodes
 
# Pin 7 is GPIO pin 4
speed = 0.25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
pin11 = GPIO.PWM(11, 100)
pin7 = GPIO.PWM(7, 100)
pin11.start(50)
pin7.start(50)

try:
    while True:
      GPIO.output(7, GPIO.HIGH)
      GPIO.output(11, GPIO.LOW)
      pin7.ChangeFrequency(523.25) # C0

except KeyboardInterrupt:
    print("CNTL-C")

except:
    print("Program Aborted")
    
finally:
    GPIO.cleanup()


if True == False:
  sleep(speed)
  pin7.ChangeFrequency(261.63) # C4
  sleep(speed)
  pin7.ChangeFrequency(293.66) # D4
  sleep(speed)
  pin7.ChangeFrequency(329.63) # E4
  sleep(speed)
  pin7.ChangeFrequency(349.23) # F4
  sleep(speed)
  pin7.ChangeFrequency(392.00) # G4
  sleep(speed)
  pin7.ChangeFrequency(440.00) # A4
  sleep(speed)
  pin7.ChangeFrequency(493.88) # B4
  sleep(speed)
  pin7.ChangeFrequency(523.25) # A5
  sleep(speed*1.5)
  pin7.ChangeFrequency(16.35) # C0
  sleep(speed)
  GPIO.output(7, GPIO.LOW)
  GPIO.output(11, GPIO.HIGH)
  sleep(speed)
