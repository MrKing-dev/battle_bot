from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event6')

print(gamepad)

southBtn = 304
eastBtn = 305
northBtn = 307
westBtn = 306
startBtn = 311
selBtn = 310
leftBump = 308
rightBump = 309

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == southBtn:
                print("A")
            elif event.code == eastBtn:
                print("B")
            elif event.code == northBtn:
                print("Y")
            elif event.code == westBtn:
                print("X")
            elif event.code == startBtn:
                print("START")
            elif event.code == selBtn:
                print("SELECT")
            elif event.code == leftBump:
                print("LEFT BUMPER")
            elif event.code == rightBump:
                print("RIGHT BUMPER")
        elif event.value == 0:
            print("RELEASED")
    
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
            if absevent.event.value == 0:
                print("Left Stick | Left")
            elif absevent.event.value == 65535:
                print("Left Stick | Right")
            elif absevent.event.value == 32768:
                print("Left Stick | Center")
        
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
            if absevent.event.value == 0:
                print("Left Stick | Up")
            elif absevent.event.value == 65535:
                print("Left Stick | Down")
            elif absevent.event.value == 32768:
                print("Left Stick | Center")
                
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":
            if absevent.event.value == 0:
                print("Right Stick | Left")
            elif absevent.event.value == 255:
                print("Right Stick | Right")
            elif absevent.event.value == 127:
                print("Right Stick | Center")
                
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RY":
            if absevent.event.value == 0:
                print("Right Stick | Up")
            elif absevent.event.value == 255:
                print("Right Stick | Down")
            elif absevent.event.value == 127:
                print("Right Stick | Center")
                
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
            print(f"Left Trigger: {absevent.event.value}")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
            print(f"Right Trigger: {absevent.event.value}")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":
            print(f"DPAD H: {absevent.event.value}")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":
            print(f"DPAD V: {absevent.event.value}")
        
    
