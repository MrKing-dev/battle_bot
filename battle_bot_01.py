import ledshim
import multiprocessing
from adafruit_motorkit import MotorKit
from time import sleep
from os import path
from evdev import InputDevice, categorize, ecodes


#DEFINE VARIABLES

kit = MotorKit()
gamepad = ""
offToggle = False
southBtn = 304
eastBtn = 305
northBtn = 308
westBtn = 307
startBtn = 315
selBtn = 314
leftBump = 310
rightBump = 311
hatY = 'ABS_HAT0Y'
hatX = 'ABS_HAT0X'
leftTrigger = 'ABS_BRAKE'
rightTrigger = 'ABS_GAS'
leftStickY = 'ABS_Y'
leftStickX = 'ABS_X'
rightStickY = 'ABS_RZ'
righStickX = 'ABS_Z'
min = 0
max = 65535

sleep(1)

#SET ALL MOTORS AND DEVICES TO INITIAL STATE
kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
light_toggle = 0

#CLASS FOR MULTITASKING - CREATES THE ABILITY TO TURN THE LIGHTS ON AND OFF WHILE DRIVING
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

#FUNCTION FOR INITIAL STARTUP INDICATOR LIGHT
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

#FUNCTION FOR RED FLASHING LIGHTS ON ERROR
def redBlink():
    ledshim.set_multiple_pixels(range(0,28), (255, 0, 0))
    ledshim.show()
    sleep(0.25)
    ledshim.clear()
    ledshim.show()
    sleep(0.25)
    ledshim.set_multiple_pixels(range(0,28), (255, 0, 0))
    ledshim.show()
    sleep(0.25)
    ledshim.clear()
    ledshim.show()
    sleep(0.5)
    
#FUNCTION FOR CONNECTING BLUETOOTH CONTROLLER WITH FAILSAFE
def checkController():
    contTrue = False
    checkPath = '/dev/input/event2'
    
    while contTrue == False:
        try:
            print("Trying to connect")
            gamepad = InputDevice(checkPath)
            print("Gamepad connected.")
            print()
            print(gamepad)
            contTrue = True
            print("Sending to startup")
            startup()
            #added
            print("Sent to startup")
            #return gamepad            
            
        except:
            print("No devices connected!")
            print()
            redBlink()
            print("Blinked")
            sleep(1)
            
            
#FUNCTION FOR MAIN DRIVE AND TOGGLING LIGHTS/ SHUTDOWN
def goBot():
    while True:
        print("In goBot")
        try:
            print("Trying to run goBot")
            gamepad = InputDevice('/dev/input/event2')
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1:
                        if event.code == southBtn:
                            print("A")
                            
                        elif event.code == leftBump:
                            print("lBump")
                            kit.motor1.throttle = -1
                        elif event.code == rightBump:
                            print("rBump")
                            kit.motor3.throttle = -1
                        elif event.code == selBtn:
                            print("Select")
                            
                            if __name__ == '__main__':
                                process = PoliceFlash()
                                if light_toggle == 0:
                                    process.start()
                                    print('Running...')
                                    light_toggle = 1
                                else:
                                    process.shutdown()
                                    print('Program shutdown')
                                    light_toggle = 0                                  
                                
                        elif event.code == startBtn:
                            print("Start")
                            redBlink()
                            kit.motor1.throttle = 0
                            kit.motor2.throttle = 0
                            kit.motor3.throttle = 0
                            offToggle = True
                            return
                        
                    elif event.value == 0:
                        if event.code == leftBump:
                            print("Released")
                            kit.motor1.throttle = 0
                        elif event.code == rightBump:
                            print("Released")
                            kit.motor3.throttle = 0
                        elif event.code == southBtn:
                            print("Released")                            
                            
                elif event.type == ecodes.EV_ABS:
                    print('Joystick movement detected')
                    normalizedX = 0.0
                    normalizedY = 0.0
                    xAxis = gamepad.absinfo(ecodes.ABS_X).value
                    print('Captured xAxis value')
                    yAxis = gamepad.absinfo(ecodes.ABS_Y).value
                    print('Captured yAxis value')
                    normalizedX = 2.0 * (xAxis - min) / (max - min) - 1.0
                    normalizedY = -(2.0 * (yAxis - min) / (max - min) - 1.0)
                    print('Normalized values')

                    print("X: " + str(normalizedX))
                    print("Y: " + str(normalizedY))
                    print()
                    rMotor = ((normalizedY) - (normalizedX))
                    lMotor = ((normalizedY) + (normalizedX))
                    if rMotor > 1.0:
                        rMotor = 1.0
                    if lMotor > 1.0:
                        lMotor = 1.0
                    if rMotor < -1.0:
                        rMotor = -1.0
                    if lMotor < -1.0:
                        lMotor = -1.0
                    print('RightMotor: ' + str(rMotor))
                    print('LeftMotor: ' + str(lMotor))

                    kit.motor3.throttle = rMotor
                    kit.motor1.throttle = lMotor

                        
                    # if ecodes.bytype[absevent.event.type][absevent.event.code] == leftStickY or ecodes.bytype[absevent.event.type][absevent.event.code] == leftStickX:
                    #     ev = absevent.event.value
                    #     normalizedY = 2.0 * (ev - min) / (max - min) - 1.0
                    
                    #elif ecodes.bytype[absevent.event.type][absevent.event.code] == leftStickX:
                        #ev = absevent.event.value
                        #nromalizedX = 2.0 * (ev - min) / (max - min) - 1.0
                        
                    #v = (1-abs(normalizedX)) * (normalizedY/1) + normalizedY
                    #w = (1-abs(normalizedY)) * (normalizedX/1) + normalizedX              
                
                    
                    #if ecodes.bytype[absevent.event.type][absevent.event.code] == leftTrigger:
                       # ev = absevent.event.value
                       # if ev > 1000:
                       #     ev = 1000
                       # print(ev/1000)
                      #  kit.motor1.throttle = ev/1000
                        
                #    elif ecodes.bytype[absevent.event.type][absevent.event.code] == rightTrigger:
                    #    ev = absevent.event.value
                     #   if ev > 1000:
                      #      ev = 1000
                       # print(ev/1000)
                       # kit.motor3.throttle = ev/1000        
        except:
            print("Gamepad disconnected! Please reconnect.")
            kit.motor1.throttle = 0
            kit.motor3.throttle = 0
            checkController()

#MAIN LOOP
print("Testing for bluetooth controller.")
print()
checkController()
goBot()
quit()


