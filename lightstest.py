import ledshim
from time import sleep

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
    
while True:
    startup()