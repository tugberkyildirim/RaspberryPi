# AnalogRead Python Module

## Overview
The `AnalogRead` module is a Python class designed for reading analog values from a specified ADC (Analog-to-Digital Converter) pin on a **Rasberry Pi Pico**. This class allows you to read raw analog values and map them to a different range for more meaningful data representation.

## Features
- Initialize the ADC on a specified pin.
- Read analog values and scale them to a specified range.
- Map values from one range to another.

## Dependencies
- `machine`: For interfacing with hardware.
- `utime`: For handling time delays.

## Default Values
- `Analog Pin: GP26, pin number 31 on pi pico`
- `read(max_val=1023,in_max=65535):`

## Installation
Ensure that you have the required dependencies installed and that you are using a compatible microcontroller.

## Usage
   ```
   from AnalogRead import AnalogRead
   import utime
   analog_value=AnalogRead()
   while True:
      val=analog_value.read()
      map_val=analog_value.map_value(val,0,1023,0,100)
      print("VALUE: "+str(val)+" MAP: "+str(map_val))
      utime.sleep(.1)
   ```
