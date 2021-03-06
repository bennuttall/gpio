from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS = [2, 3, 4, 14, 15, 17, 18, 27, 22, 23, 24, 10, 9, 25, 11, 8, 7, 5, 6, 12, 13, 19, 16, 26, 20, 21]


def gpio_setup():
    """
    Setup all GPIO pins in the list as outputs.
    """

    for pin in PINS:
        GPIO.setup(pin, GPIO.OUT)


def all_on(step=0, reverse=False):
    """
    Set each GPIO pin to high in sequence (reversed if `reverse` is True) with
    a pause between each one of a number of seconds given in `step`.
    """

    pins = reversed(PINS) if reverse else PINS

    for pin in pins:
        GPIO.output(pin, True)
        print("pin %2.0f on" % pin)
        sleep(step)


def all_off(step=0, reverse=False):
    """
    Set each GPIO pin to low in sequence (reversed if `reverse` is True) with
    a pause between each one of a number of seconds given in `step`.
    """

    pins = reversed(PINS) if reverse else PINS

    for pin in pins:
        GPIO.output(pin, False)
        print("pin %2.0f off" % pin)
        sleep(step)


def main():
    gpio_setup()

    print('')

    while True:
        all_on(step=0.1)
        all_off(step=0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
