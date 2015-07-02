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

PINS = [

     2,
     3,
     4, 14,
        15,
    17, 18,
    27,
    22, 23,
        24,
    10,
     9, 25,
    11,  8,
         7,

     5,
     6, 12,
    13,
    19, 16,
    26, 20,
        21
]


def gpio_setup():
    """
    Setup all GPIO pins in the list as inputs.
    """

    for pin in PINS:
        GPIO.setup(pin, GPIO.IN, PULL)
        GPIO.add_event_detect(pin, EDGE, callback, BOUNCE)


def callback(pin):
    """
    Callback function to print which GPIO pin was pressed.
    """

    print("pin %2.0f was pressed" % pin)


def main():
    gpio_setup()

    print('')
    input("Press Enter to exit")

    GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
