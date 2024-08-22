from AnalogRead import AnalogRead
import utime
analog_value=AnalogRead()
while True:
    val=analog_value.read()
    map_val=analog_value.map_value(val,0,1023,0,100)
    print("VALUE: "+str(val)+" MAP: "+str(map_val))
    utime.sleep(.1)
