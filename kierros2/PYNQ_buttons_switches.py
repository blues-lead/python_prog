from pynq.lib import Button
from pynq.lib import Switch

def blink(x,y):
    led_matrix.set_led_color(x,y,0,255,0)
    time.sleep(0.1)
    led_matrix.set_led_color(x,y,0,0,0)
    return

def main():
    led_matrix.init()
    blink(0,0)
    
    
main()