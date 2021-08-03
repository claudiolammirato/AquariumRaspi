import sys
import os

from graphic import grafica

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


def main():
    grafica()
    

if __name__ == "__main__":
    main()