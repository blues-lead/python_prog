import tut.arduino_led_matrix as led_matrix
import time

def main():
    # a) ######################################################
    led_matrix.init()
    for i in range(0,8):
        for j in range(0,8):
            led_matrix.set_led_color(i,j,0,255,0)
            time.sleep(0.02)
            led_matrix.set_led_color(i,j,0,0,0)
    time.sleep(0.5)
    ###########################################################
    # b) ######################################################
    for z in range(0,8):
        led_matrix.set_led_color(1,z,0,255,0) #first raw ignited
    for i in range(1,8):
        for j in range(0,8):
            led_matrix.set_led_color(i,j,0,255,0)
            led_matrix.set_led_color(i-1,j,0,0,0)
        time.sleep(0.1)

    for z in range(0,8):
        led_matrix.set_led_color(7,z,0,0,0)
    time.sleep(0.5)
    ###########################################################
    # c) ######################################################
    for i in range(0,8):
        led_matrix.set_led_color(0,i,0,255,0)
        time.sleep(0.1)
        led_matrix.set_led_color(0,i,0,0,0)
    #time.sleep(0.1)
    for i in range(0,8):
        led_matrix.set_led_color(i,7,0,255,0)
        time.sleep(0.1)
        led_matrix.set_led_color(i,7,0,0,0)
    #time.sleep(0.1)
    for i in range(7,-1,-1):
        led_matrix.set_led_color(7,i,0,255,0)
        time.sleep(0.1)
        led_matrix.set_led_color(7,i,0,0,0)
    for i in range(7,-1,-1):
        led_matrix.set_led_color(i,0,0,255,0)
        time.sleep(0.1)
        led_matrix.set_led_color(i,0,0,0,0)
    time.sleep(0.5)
    ###########################################################
    # d) ######################################################
    led_matrix.init()
    for z in range(0,8):
        i = 0
        j = z
        while i <= 8 and j >= 0:
            led_matrix.set_led_color(i,j,0,255,0)
            i+=1
            j-=1
        time.sleep(0.2)
        i = 0
        j = z
        while i <= 8 and j >= 0:
            led_matrix.set_led_color(i,j,0,0,0)
            i+=1
            j-=1
    for z in range(1,8):
        i = 7
        j = z
        while i >= 1 and j <=7:
            #print(i,j)
            led_matrix.set_led_color(i,j,0,255,0)
            i-=1
            j+=1
        time.sleep(0.2)
        i = 7
        j = z
        while i >= 1 and j <=7:
            #print(i,j)
            led_matrix.set_led_color(i,j,0,0,0)
            i-=1
            j+=1
            
    
main()