import os
from time import sleep
while True:
    q = input('target ')
    print()
    print(q + 'is the target')
    sleep(1.2)
    for thrdf in range (10):
        print('00101101101010010101001010101001010100101001010110101001')
        sleep(0.15)
        print('11010101000101010101010100100101010010100101001010010101')
        sleep(0.15)
        print('00101010100100101010100100101010010101001000001011111010')
        sleep(0.15)
        print('11101010101110100101010100101010100101010010101010010010')
        sleep(0.15)
        print('01010100010111110101010010011110101001011010010010010101')
        sleep(0.15)
    print('grabbing os import...')
    sleep(2)
    print('getting batch....')
    sleep(8)
    print()
    print('OK. PING OF DETH DETECTOR IS READY')
    print()
    print()
    bts = 50
    print('_' * 10)
    change = input('change bytes ')
    print('_' * 10)
    for x in range (200):
        print('start test ' + str(bts))
        os.system('ping ' + q + ' -n 1 -l ' + str(bts))
        print()
        print()
        print('_' * 25)
        print(str(bts) + ' bytes sent to host ' + q)
        print('-' * 25)
        print()
        bts = bts + change
        sleep(6)

