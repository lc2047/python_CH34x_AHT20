#!/usr/bin/python3

class CH341_I2Cpy:
    def __init__(self):
        from i2cpy import I2C
        self.CH341_i2c = I2C(id=0, driver="ch341")
        # print(f'print in i2c_channel.py/CH341_I2Cpy/__init__ : {self.CH341_i2c} ')
        # print(f'print in i2c_channel.py/CH341_I2Cpy/__init__ : None ')

    def scan(self):
        return self.CH341_i2c.scan()

    def read(self, addr, nBytes):
        return self.CH341_i2c.readfrom(addr, nBytes)

    def read_mem(self, addr=0, memAddr=0, nBytes=1):
        return self.CH341_i2c.readfrom_mem(addr, memAddr, nBytes)

    def write(self, addr, data):
        return self.CH341_i2c.writeto(addr, data)

    def write_mem(self, addr=0, memAddr=0, data=0):
        return self.CH341_i2c.writeto_mem(addr, memAddr, data)


class CH347_I2Cpy:
    def __init__(self):
        from i2cpy import I2C
        self.CH347_i2c = I2C(id=0, driver="ch347")
        # print(f'print in i2c_channel.py/CH347_I2Cpy/__init__ : {self.CH347_i2c} ')
        # print(f'print in i2c_channel.py/CH347_I2Cpy/__init__ : None ')

    def scan(self):
        return self.CH347_i2c.scan()

    def read(self, addr, nBytes):
        return self.CH347_i2c.readfrom(addr, nBytes)

    def read_mem(self, addr=0, memAddr=0, nBytes=1):
        return self.CH347_i2c.readfrom_mem(addr, memAddr, nBytes)

    def write(self, addr, data):
        return self.CH347_i2c.writeto(addr, data)

    def write_mem(self, addr=0, memAddr=0, data=0):
        return self.CH347_i2c.writeto_mem(addr, memAddr, data)


if __name__ == '__main__':
    #ch = CH341_I2Cpy()
    ch = CH347_I2Cpy()

    print('-' * 5 + '  I2C  SCAN  ' + '-' * 5)
    number_devices = ch.scan()
    print(f'{len(number_devices)} devices found :', end=' ')
    for device in number_devices:
        print(f'0x{device:X}', end=' ')
    print()

    print('-' * 5 + '  I2C  READ  ' + '-' * 5)
    data = ch.read(addr=0x38, nBytes=6)
    print(f'read {len(data)} byte(s) data :', end=' ')
    for member in data:
        print(f'0x{member:X}', end=' ')
    print()

    print('-' * 5 + ' I2C READ MEM ' + '-' * 5)
    data = ch.read_mem(addr=0x38, memAddr=0x04, nBytes=2)
    print(f'read {len(data)} byte(s) data :', end=' ')
    for member in data:
        print(f'0x{member:X}', end=' ')
    print()
    '''
    print('-' * 5 + ' I2C WRIT MEM ' + '-' * 5)
    data = ch.read_mem(addr=0x38, memAddr=0x05, nBytes=2)
    print(f'read {len(data)} byte(s) data :', end=' ')
    for member in data:
        print(f'0x{member:X}', end=' ')
    print()
    data = b'\xAA\xBB\xCC\xDD\xEE'
    ch.write_mem(addr=0x38, memAddr=0x05, data=data)
    print(f'write {len(data)} byte(s) data :', end=' ')
    for member in data:
        print(f'0x{member:X}', end=' ')
    print()
    '''