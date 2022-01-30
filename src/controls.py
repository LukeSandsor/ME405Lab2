'''!
@file controls.py
This file contains necessary methods and attributes for closed
loop control of motor
@author Lucas Sandsor
@author Jack Barone
@author Jackson Myers
@date 25-Jan-2022 
'''
import pyb
class Controls:
    '''!
    This class impliments the motor controller for ME405
    '''
    def __init__(self, setpoint, gain, error_signal):
        '''!
        Creates an encoder driver by initializing GPIO
        pins and reading signal output from two channels and comparing
        them to see what the direction of movement is
        @param !!!DO LATER
        @param    gain has units percent duty cycle per encoder count
        '''
        self.setpoint = setpoint
        self.gain = gain
        self.error_signal = error_signal
        self.time_list = []
        self.tick_list = []
        

    def controlLoop(self, position):
        self.error_signal = self.setpoint - position
        actuation = self.error_signal * self.gain
        return actuation

    def set_setpoint(self, new_setpoint):
        '''!
        @param    new_point
        '''
        self.setpoint = new_setpoint
        
    def set_gain(self, new_gain):
        '''!
        '''
        self.gain = new_gain
        
    def print_list(self, time_ms, ticks):
        '''!
        '''
        print(time_ms, ticks)
        
    def store_list(self, time_ms, ticks):
        '''!
        '''
        self.time_list.append(time_ms)
        self.tick_list.append(ticks)
        
        
    

        
