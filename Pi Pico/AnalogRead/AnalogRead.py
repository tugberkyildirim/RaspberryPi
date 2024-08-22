import machine,utime

class AnalogRead():
    def __init__(self,analog_pin=26):
      self.analog_pin=machine.ADC(analog_pin)

    def read(self,max_val=1023,in_max=65535):
     val=int(self.analog_pin.read_u16())
     utime.sleep(.1)
     return int((val - 0) * (max_val - 0) / (in_max - 0) + 0)


    def map_value(self,val, in_min,in_max, out_min,out_max):
      return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    
