from signal import signal, SIGINT
import sys
from threading import Thread
from time import sleep

from pynput.keyboard import HotKey, Listener
from pynput.mouse import Controller, Button

# globals; a const is below because python sux
mouse = Controller()
click = lambda : mouse.click(Button.left)
is_clicking = False
click_latency = 0.02

# interrupt handler
def irq(signum, frame):

    print("\ninterrupted! exiting...")
    sys.exit(0)

# print usage for incorrect inputs
def usage_print():

    print("usage: clkmacro.py [cps]\nargs:\n\n\tcps: clicks per second. cannot be 0\n")

# functions to toggle global click state
# both used by pynput for detecting entered macro
def set_click():

    global is_clicking
    is_clicking = not is_clicking

def for_canonical(f): # i dont know why this function is needed this is from the pynput docs

    return lambda k: f(l.canonical(k))

# main program loop
def click_loop():

    global is_clicking
    global click_latency
    while True:

        if is_clicking:
            click()
        
        sleep(click_latency)

KEY_MACRO = HotKey(HotKey.parse('<ctrl>+`'), set_click)

if __name__ == "__main__":

    if len(sys.argv) > 2:
        usage_print()
        sys.exit(1)

    # set CPS if specified
    if len(sys.argv) == 2:
        try:
            click_latency = 1 / float(sys.argv[1])
        except:
            usage_print()
            sys.exit(1)

    signal(SIGINT, irq)

    # shouldn't actually use daemon
    # but its so easy to SIGINT cleanup daemons
    Thread(target = click_loop, daemon=True).start()

    with Listener(
            on_press=for_canonical(KEY_MACRO.press),
            on_release=for_canonical(KEY_MACRO.release)
            ) as l:
        l.join()
