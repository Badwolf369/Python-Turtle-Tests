from time import sleep
from random import uniform

def write(text):
    for c in text:
        print(c, end='', flush=True)
        sleep(uniform(0.2, 0.1))
    print('')

write('This is a test of being able to commit changes in a branch')
