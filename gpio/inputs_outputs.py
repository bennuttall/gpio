from RPi import GPIO
from time import sleep

# Fix for Python 2
try:
    input = raw_input
except NameError:
    pass

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PULL = GPIO.PUD_UP
EDGE = GPIO.FALLING
BOUNCE = 1000

INPUT_PINS = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26] # inside pins
OUTPUT_PINS = [14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21] # outside pins

def gpio_setup():
    """
    Setup all GPIO pins in the list as inputs.
    """

    for pin in INPUT_PINS:
        GPIO.setup(pin, GPIO.IN, PULL)
        GPIO.add_event_detect(pin, EDGE, callback, BOUNCE)

    for pin in OUTPUT_PINS:
        GPIO.setup(pin, GPIO.OUT)


def callback(pin):
    """
    Callback function to print which GPIO pin was pressed.
    """

    print("pin %2.0f was pressed")


def all_outputs_on(step=0, reverse=False):
    """
    Set each GPIO output pin to high in sequence (reversed if `reverse` is
    True) with a pause between each one of a number of seconds given in `step`.
    """

    pins = reversed(OUTPUT_PINS) if reverse else OUTPUT_PINS

    for pin in pins:
        GPIO.output(pin, True)
        print("pin %2.0f on" % pin)
        sleep(step)


def all_outputs_off(step=0, reverse=False):
    """
    Set each GPIO output pin to low in sequence (reversed if `reverse` is True)
    with a pause between each one of a number of seconds given in `step`.
    """

    pins = reversed(OUTPUT_PINS) if reverse else OUTPUT_PINS

    for pin in pins:
        GPIO.output(pin, False)
        print("pin %2.0f off" % pin)
        sleep(step)


def main():
    gpio_setup()

    print('')

    while True:
        all_outputs_on(step=2)
        all_outputs_off(step=2)

    GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
