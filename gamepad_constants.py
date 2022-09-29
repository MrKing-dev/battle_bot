from evdev import InputDevice, categorize, ecodes
import explorerhat

gamepad = InputDevice('/dev/input/event2')


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



