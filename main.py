import sys
import os
import threading 

from graphic import grafica
import schedule
import time
from dht_aquarium import retrieve_temp_hum_ext
from sqlite import create_table
from ds18_aquarium import retrieve_temp_int

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


def main():

    #check if database ok
    create_table()

    
        
    p1 = threading.Thread(target=grafica)
    p2 = threading.Thread(target=retrieve_temp_hum_ext)
    p3 = threading.Thread(target=retrieve_temp_int)
    p1.start()
    p2.start()
    p3.start()

   

if __name__ == "__main__":
    main()





