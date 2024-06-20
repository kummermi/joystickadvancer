motorPowerX = 0
advancerDrive.zero_all_motors()
advancerDrive.write_all()
xZeroOffset = pins.analog_read_pin(AnalogPin.P0)
yZeroOffset = pins.analog_read_pin(AnalogPin.P1)
basic.show_number(xZeroOffset)

def on_every_interval():
    global motorPowerX
    motorPowerX = (pins.analog_read_pin(AnalogPin.P0) - xZeroOffset) / 2.5
    basic.show_number(motorPowerX)
    advancerDrive.set_motor_power(1, motorPowerX)
    advancerDrive.write_all()
loops.every_interval(100, on_every_interval)
