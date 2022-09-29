import explorerhat
from time import sleep
import gamepad_constants as gp
from evdev import InputDevice, categorize, ecodes

#blue, yellow, red, green

m1 = explorerhat.motor.one
m2 = explorerhat.motor.two

for event in gp.gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == gp.southBtn:
                explorerhat.light.blue.on()
            elif event.code == gp.eastBtn:
                explorerhat.light.yellow.on()
            elif event.code == gp.northBtn:
                explorerhat.light.red.on()
            elif event.code == gp.westBtn:
                explorerhat.light.green.on()
            elif event.code == gp.startBtn:
                explorerhat.light.red.off()
                explorerhat.light.yellow.off()
                explorerhat.light.blue.off()
                explorerhat.light.green.off()
            elif event.code == gp.selBtn:
                explorerhat.light.red.off()
                explorerhat.light.yellow.off()
                explorerhat.light.blue.off()
                explorerhat.light.green.off()
            elif event.code == gp.leftBump:
                explorerhat.light.blue.on()
                explorerhat.light.yellow.on()
            elif event.code == gp.rightBump:
                explorerhat.light.red.on()
                explorerhat.light.green.on()
                
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
            if absevent.event.value == 0:
                m1.forwards()
                m2.backwards()
                print("Left Stick | Left")
            elif absevent.event.value == 65535:
                m1.backwards()
                m2.forwards()
                print("Left Stick | Right")
            elif absevent.event.value == 32768:
                m1.stop()
                m2.stop()
                print("Left Stick | Center")
        
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
            if absevent.event.value == 0:
                m1.forwards()
                m2.forwards()
                print("Left Stick | Up")
            elif absevent.event.value == 65535:
                m1.backwards()
                m2.backwards()
                print("Left Stick | Down")
            elif absevent.event.value == 32768:
                m1.stop()
                m2.stop()
                print("Left Stick | Center")



#while True:
    #explorerhat.touch.pressed(handle_pin)