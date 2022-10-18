import ledshim
import multiprocessing
from adafruit_motorkit import MotorKit
from time import sleep
from os import path
from evdev import InputDevice, categorize, ecodes

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
gamepad = InputDevice('/dev/input/event2')
min = 0
max = 65535

def joystickTest():
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
                                
                        elif event.code == startBtn:
                            print("Start")
                                                    
                    elif event.value == 0:
                        if event.code == leftBump:
                            print("Released")
                        elif event.code == rightBump:
                            print("Released")
                        elif event.code == southBtn:
                            print("Released")                            
                            
                elif event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    normalizedX = 0.0
                    normalizedY = 0.0
                        
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == leftStickY:
                        ev = absevent.event.value
                        normalizedY = 2.0 * (ev - min) / (max - min) - 1.0
                    
                    elif ecodes.bytype[absevent.event.type][absevent.event.code] == leftStickX:
                        ev = absevent.event.value
                        normalizedX = 2.0 * (ev - min) / (max - min) - 1.0
                        
                    v = (1-abs(normalizedY)) * (normalizedX/1) + normalizedX
                    w = (1-abs(normalizedX)) * (normalizedY/1) + normalizedY
                    
                    r = (v+w)/2
                    l = (v-w)/2
                    #print("V: " + str(v))
                    #print("W: " + str(w))
                    #print("R: " + str(r))
                    #print("L: " + str(l))
                    kit.motor3.throttle

                        
joystickTest()
