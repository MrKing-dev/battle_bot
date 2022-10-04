import ledshim
import multiprocessing
import RPi.GPIO as GPIO
#from adafruit_motorkit import MotorKit
from time import sleep
import gamepad_constants as gp
from evdev import InputDevice, categorize, ecodes

#blue, yellow, red, green

kit = MotorKit()
#m1 = kit.motor1 #left motor
#m2 = kit.motor2 # right motor

kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
light_toggle = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
pin11 = GPIO.PWM(11, 100)
pin7 = GPIO.PWM(7, 100)
pin11.start(50)
pin7.start(50)

class BackupBeep(multiprocessing.Process):
    
    def __init__(self, ):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()
    
    def run(self):
        while not self.exit.is_set():
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(11, GPIO.LOW)
            
            pin7.ChangeFrequency(523.25)
            sleep(1)
            
            GPIO.output(7, GPIO.LOW)
            sleep(1)
            
    def shutdown(self):
        GPIO.output(7, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.cleanup()

class PoliceFlash(multiprocessing.Process):

    def __init__(self, ):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()

    def run(self):
        while not self.exit.is_set():
            ledshim.set_multiple_pixels(range(0, 14), (0, 100, 255))    
            ledshim.show()
        
            sleep(0.25)
                
            ledshim.clear()
            ledshim.show()
            
            
            ledshim.set_multiple_pixels(range(14, 28), (255, 0, 0))    
            ledshim.show()
        
            sleep(0.25)
                
            ledshim.clear()
            ledshim.show()
        
        ledshim.clear()
        ledshim.show()
        print('police aborted')
        
            
    def shutdown(self):
        print('police stopped')
        self.exit.set()


def startup():
    ledshim.set_multiple_pixels(range(0, 7), (0, 100, 255))    
    ledshim.show()
    
    sleep(0.25)
    
    ledshim.set_multiple_pixels(range(8, 14), (240, 255, 0))    
    ledshim.show()
    
    sleep(0.25)
    
    ledshim.set_multiple_pixels(range(15, 21), (255, 0, 0))    
    ledshim.show()
    
    sleep(0.25)
    
    ledshim.set_multiple_pixels(range(22, 28), (0, 255, 0))    
    ledshim.show()
    
    sleep(1)
    
    ledshim.clear()
    ledshim.show()

    
startup()

for event in gp.gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == gp.southBtn:
                print("A")
                if __name__ == '__main__':
                    process = BackupBeep()
                    process.start()
                    print('Running...')
                    
            elif event.code == gp.leftBump:
                print("lBump")
                kit.motor1.throttle = -1
            elif event.code == gp.rightBump:
                print("rBump")
                kit.motor3.throttle = -1
            elif event.code == gp.selBtn:
                print("Select")
                
                if __name__ == '__main__':
                    if light_toggle == 0:
                        process = PoliceFlash()
                        process.start()
                        print('Running...')
                        light_toggle = 1
                    else:
                        process.shutdown()
                        print('Program shutdown')
                        light_toggle = 0
                        
                    
            elif event.code == gp.startBtn:
                print("Start")
                ledshim.set_multiple_pixels(range(0,28), (255, 0, 0))
                ledshim.show()
                sleep(0.5)
                ledshim.clear()
                ledshim.show()
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                kit.motor3.throttle = 0
                quit()
            
        elif event.value == 0:
            if event.code == gp.leftBump:
                print("Released")
                kit.motor1.throttle = 0
            elif event.code == gp.rightBump:
                print("Released")
                kit.motor3.throttle = 0
            elif event.code == gp.southBtn:
                print("Released")
                if __name__ == '__main__':
                    process = BackupBeep()
                    process.shutdown()
                    print('Beeping Stopped...')
                
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
        #    if absevent.event.value == 0:
        #        m2.forwards()
        #        m1.backwards()
         #       print("Left Stick | Left")
         #   elif absevent.event.value == 65535:
        #        m2.backwards()
          #      m1.forwards()
         #       print("Left Stick | Right")
          #  elif absevent.event.value == 32768:
       #         m1.stop()
        #        m2.stop()
         #       print("Left Stick | Center")
                
        if ecodes.bytype[absevent.event.type][absevent.event.code] == gp.leftTrigger:
            ev = absevent.event.value
            if ev > 1000:
                ev = 1000
            print(ev/1000)
            kit.motor1.throttle = ev/1000
            
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == gp.rightTrigger:
            ev = absevent.event.value
            if ev > 1000:
                ev = 1000
            print(ev/1000)
            kit.motor3.throttle = ev/1000        
       # elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
         #   if absevent.event.value == 0:
         #       m1.forwards()
          #      m2.forwards()
          #      print("Left Stick | Up")
           # elif absevent.event.value == 65535:
         #       m1.backwards()
          #      m2.backwards()
         #       print("Left Stick | Down")
         #   elif absevent.event.value == 32768:
          #      m1.stop()
           #     m2.stop()
          #      print("Left Stick | Center")



#while True:
    #explorerhat.touch.pressed(handle_pin)
