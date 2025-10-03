#!/usr/bin/python3

default_addr = 0x38
# Initialize the AHT20 sensor (recommended for stability)
initialize = b'\xBE\x08'

# Trigger measurement command
# 0xAC: Command to trigger measurement
# 0x33, 0x00: Parameters
Trigger_measurement = b'\xAC\x33\x00'


class AHT20:
    def __init__(self, i2c_channel, address=default_addr):
            self.AHT20_address          = address
            self.AHT20_i2c              = i2c_channel
            self.calibrated             = False
            self.last_temperature       = 0.0
            self.last_humidity          = 0.0
            self.is_initialized         = False
            self.is_Trigger_measurement = False

    def write(self, data):
            return self.AHT20_i2c.write(self.AHT20_address, data)

    def read(self,dataLength=6):
        return self.AHT20_i2c.read(self.AHT20_address, dataLength)

    def initialize(self):
        try:
            self.write(initialize)
            self.calibrated         = True
            self.is_initialized     = True
            #print(f'AHT20 success to initialize')
            return self.is_initialized
        except Exception as e:
            #print(f"Error: AHT20 to initialize : {e}")
            return self.is_initialized

    def Trig_Meas(self):
        try:
            self.write(Trigger_measurement)
            self.is_Trigger_measurement = True
            #print(f'AHT20 success to Triggered Measurement mode')
            return self.is_Trigger_measurement
        except Exception as e:
            self.is_Trigger_measurement = False
            #print(f"Error: AHT20 to enter Trigger Measurement : {e}")
            return self.is_Trigger_measurement

    def data_transform(self, data):
        # Parse the raw data according to the AHT20 datasheet
        # Humidity is a 20-bit value spread across bytes 1, 2, and 3
        # raw_humidity = ((data[1] & 0x0F) << 16) | (data[2] << 8) | data[3]
        raw_humidity = (data[1] << 12) | (data[2] << 4) | (data[3] >> 4)
        humidity = (raw_humidity * 100) / 0x100000
        #print("Humidity : %.2f%%" % humidity)

        # Temperature is a 20-bit value spread across bytes 3, 4, and 5
        raw_temperature = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
        temperature = (raw_temperature * 200) / 0x100000 - 50
        #print(f'Temperature : {temperature:.2f}')

        return humidity, temperature


if __name__ == "__main__":
    from i2c_Channel import CH347_I2Cpy, CH341_I2Cpy
    import time

    AHT20_i2c = CH341_I2Cpy()
    #AHT20_i2c = CH347_I2Cpy()
    #print(f'print in aht20.py/main : {AHT20_i2c} ')
    a = AHT20(AHT20_i2c, 0x38)

    if (a.initialize() == True ):
        print(f'AHT20 success to initialize')
    else:
        print(f"Error: AHT20 to initialize ")

    #time.sleep(0.01)

    if (a.Trig_Meas() == True ):
        print(f'AHT20 success to Triggered Measurement mode')
    else:
        print(f"Error: AHT20 to enter Trigger Measurement ")

    #time.sleep(0.01)
    rawData = a.read(6)
    print(f'raw data : {rawData}')
    humidity, temperature = a.data_transform(rawData)

    print("Humidity : %.2f%%" % humidity)
    print(f'Temperature : {temperature:.2f}°C ')