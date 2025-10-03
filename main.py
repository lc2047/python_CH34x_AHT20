#!/usr/bin/python3

import time
from i2c_Channel import CH341_I2Cpy, CH347_I2Cpy
from aht20 import AHT20

main_I2C = CH341_I2Cpy()
#main_I2C = CH347_I2Cpy()

print('-' * 5 + '  I2C  SCAN  ' + '-' * 5)
device_list = main_I2C.scan()
print(f'{len(device_list)} devices found :', end=' ')
for device in device_list:
    print(f'0x{device:X}', end=' ')
print()

print('-' * 5 + ' AHT20 test  ' + '-' * 5)
aht20Sensor = AHT20(main_I2C, 0x38)
aht20Sensor.initialize()
aht20Sensor.Trig_Meas()

humidity, temperature = aht20Sensor.data_transform(aht20Sensor.read())
print("Humidity : %.2f%%" % humidity)
print(f'Temperature : {temperature:.2f}°C ')

