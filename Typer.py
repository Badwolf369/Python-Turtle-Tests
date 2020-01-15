from time import sleep
from random import uniform

def write(text):
    """Prints given string one character at a time with slight delay"""
    for c in text:
        print(c, end='', flush=True)
        sleep(uniform(0.2, 0.1))
    print('')