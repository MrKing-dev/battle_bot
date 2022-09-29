import explorerhat
from time import sleep


pin1 = 0
pin2 = 0
pin3 = 0
pin4 = 0

pin_number = 1234
pin_input = '0000'

def blinky(blink_speed, duration):
    explorerhat.light.yellow.blink(blink_speed, blink_speed)
    explorerhat.light.blue.blink(blink_speed, blink_speed)
    explorerhat.light.red.blink(blink_speed, blink_speed)
    explorerhat.light.green.blink(blink_speed, blink_speed)
    sleep(duration)
    explorerhat.light.yellow.off()
    explorerhat.light.blue.off()
    explorerhat.light.red.off()
    explorerhat.light.green.off()

def handle_pin(channel, event):
    global pin1
    global pin2
    global pin3
    global pin4
    global pin_input
    global pin_number
    
    print('Button Pressed')
    if event == 'press':
        if pin1 == 0:
            print('Setting pin1')
            pin1 = channel
        elif pin2 == 0:
            print('Setting pin2')
            pin2 = channel
        elif pin3 == 0:
            print('Setting pin3')
            pin3 = channel
        elif pin4 == 0:
            print('Setting pin4')
            pin4 = channel
            print('Setting pin_input')
            print(pin_input)
            pin_input_list = list(pin_input)
            print(pin_input_list)
            pin_input_list[0] = pin1
            print(pin_input_list)
            pin_input_list[1] = pin2
            print(pin_input_list)
            pin_input_list[2] = pin3
            print(pin_input_list)
            pin_input_list[3] = pin4
            print(pin_input_list)
            pin_input_string = [str(integer) for integer in pin_input_list]
            pin_input_s = ''.join(pin_input_string)
            print(pin_input_s)
            pin_input_int = int(pin_input_s)
            print(pin_input_int)
            print(f'Pin Number = {pin_number}')
            print(f'Input = {pin_input_int}')
            
            if pin_input_int == pin_number:
                print('Correct pin')
                blinky(0.2, 2)
                pin_input = '0000'
                pin1 = 0
                pin2 = 0
                pin3 = 0
                pin4 = 0
            else:
                print('Incorrect pin')
                explorerhat.light.red.pulse(0.5, 0.5, 1, 1)
                sleep(3)
                explorerhat.light.red.off()
                pin_input = '0000'
                pin1 = 0
                pin2 = 0
                pin3 = 0
                pin4 = 0

