let motorPowerX = 0
let xZeroOffset = pins.analogReadPin(AnalogPin.P0)
let yZeroOffset = pins.analogReadPin(AnalogPin.P1)
basic.showNumber(xZeroOffset)
loops.everyInterval(100, function () {
    motorPowerX = (pins.analogReadPin(AnalogPin.P0) - xZeroOffset) / 1
    motor.MotorRun(motor.Motors.M1, motor.Dir.CW, motorPowerX)
})
