import ledshim
import multiprocessing
from time import sleep

class MyProcess(multiprocessing.Process):

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
        

if __name__ == '__main__':
    process = MyProcess()
    process.start()
    print('Running...')
    sleep(5)
    process.shutdown()
    print('Program shutdown')
    
    