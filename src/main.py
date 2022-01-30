"""!@file main.py
    @brief main file responsible for functions used in Lab 2
    @detail This file contains all the funcitons for controlling
    motor speed and couting revolutions via an encoder
    attatched to the motor
    @author Lucas Sandsor
    @author Jack Barone
    @author Jackson Myers
    @date 25-Jan-2022 
"""
import motorDriver
import encoderDriver
import controls
import pyb
import utime


if __name__ == "__main__":
    '''Initialize motor and encoder drivers and then run the motor
    back and forth to see if the drivers and their methods were working
    properly.
    '''
    moe = motorDriver.MotorDriver(pyb.Pin.board.PA10,
        pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    '''To get the motor to start to move the minumum duty cycle is 25 in either
    direction but to keep it moving once started, the minimum duty cycle is
    18'''
    enc = encoderDriver.EncoderDriver(pyb.Pin.board.PB6,pyb.Pin.board.PB7, 4)
    setpoint = 8192
    controller = controls.Controls(8192, 2000/8192, 0)
    enc.zero()
    '''50/4096 means that the motor will run at half speed when it
    is two rotation
    '''
    while(input() != 'c'):
        start_time = utime.ticks_ms();
        while(utime.ticks_diff(utime.ticks_ms(), start_time) <  500):
            #An infinite loop to see it go back and forth for testing
            moe.set_duty_cycle(controller.controlLoop(enc.read()))
            #print("UPDATING")
            utime.sleep_ms(10)
            controller.store_list(utime.ticks_diff(utime.ticks_ms(), start_time), enc.read())
        moe.set_duty_cycle(0)
        enc.zero()
    moe.set_duty_cycle(0)
    for i in range(len(controller.time_list)):
            print(controller.time_list[i], end='')
            print(',', end = '')
            print(controller.tick_list[i])
            #manually sent EOF
    print(b'EOF')


            
        

           




