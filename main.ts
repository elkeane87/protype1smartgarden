let Humidity = 0
let Temperature = 0
let Dust = 0
let Uv = 0
let Wind = 0
let Moisture = 0
let DryLimit = 400
let PumpTime = 3000
let WaitTime = 60000
pins.digitalWritePin(DigitalPin.P13, 0)
OLED.init(128, 64)
OLED.clear()
OLED.writeStringNewLine("Smart Garden")
basic.pause(100)
OLED.writeStringNewLine("Starting")
basic.pause(100)
led.enable(false)
basic.forever(function () {
    Moisture = pins.analogReadPin(AnalogPin.P4)
    Wind = Environment.ReadWindSpeed(AnalogPin.P1)
    Uv = Environment.UVLevel(AnalogPin.P2)
    Dust = Environment.ReadDust(DigitalPin.P6, AnalogPin.P3)
    Temperature = Environment.dht11value(Environment.DHT11Type.DHT11_temperature_C, DigitalPin.P10)
    basic.pause(2000)
    Humidity = Environment.dht11value(Environment.DHT11Type.DHT11_humidity, DigitalPin.P10)
    OLED.clear()
    OLED.writeStringNewLine("Soil:" + ("" + Moisture))
    OLED.writeStringNewLine("Temp" + ("" + Temperature))
    OLED.writeStringNewLine("Hum:" + ("" + Humidity))
    OLED.writeStringNewLine("UV:" + ("" + Uv))
    OLED.writeStringNewLine("Wind:" + ("" + Wind))
    OLED.writeStringNewLine("Dust:" + ("" + Dust))
    basic.pause(1000)
    if (Moisture < DryLimit) {
        basic.showString("Watering")
        pins.digitalWritePin(DigitalPin.P13, 1)
        basic.pause(PumpTime)
        pins.digitalWritePin(DigitalPin.P13, 0)
        basic.showString("Watered")
        basic.pause(WaitTime)
    } else {
        pins.digitalWritePin(DigitalPin.P13, 0)
        basic.showString("Soil Ok")
        basic.pause(5000)
    }
})
