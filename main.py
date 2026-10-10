Humidity = 0
Temperature = 0
Dust = 0
Uv = 0
Wind = 0
Moisture = 0
DryLimit = 400
PumpTime = 3000
WaitTime = 60000
pins.digital_write_pin(DigitalPin.P13, 0)
OLED.init(128, 64)
OLED.clear()
OLED.write_string_new_line("Smart Garden")
basic.pause(100)
OLED.write_string_new_line("Starting")
basic.pause(100)
led.enable(False)

def on_forever():
    global Moisture, Wind, Uv, Dust, Temperature, Humidity
    Moisture = pins.analog_read_pin(AnalogPin.P0)
    Wind = Environment.read_wind_speed(AnalogPin.P1)
    Uv = Environment.uv_level(AnalogPin.P2)
    Dust = Environment.read_dust(DigitalPin.P3, AnalogPin.P4)
    Temperature = Environment.dht11value(Environment.DHT11Type.DHT11_TEMPERATURE_C, DigitalPin.P10)
    basic.pause(2000)
    Humidity = Environment.dht11value(Environment.DHT11Type.DHT11_HUMIDITY, DigitalPin.P10)
    OLED.clear()
    OLED.write_string_new_line("Soil:" + ("" + str(Moisture)))
    OLED.write_string_new_line("Temp" + ("" + str(Temperature)))
    OLED.write_string_new_line("Hum:" + ("" + str(Humidity)))
    OLED.write_string_new_line("UV:" + ("" + str(Uv)))
    OLED.write_string_new_line("Wind:" + ("" + str(Wind)))
    OLED.write_string_new_line("Dust:" + ("" + str(Dust)))
    basic.pause(1000)
    if Moisture < DryLimit:
        basic.show_string("Watering")
        pins.digital_write_pin(DigitalPin.P13, 1)
        basic.pause(PumpTime)
        pins.digital_write_pin(DigitalPin.P13, 0)
        basic.show_string("Watered")
        basic.pause(WaitTime)
    else:
        pins.digital_write_pin(DigitalPin.P13, 0)
        basic.show_string("Soil Ok")
        basic.pause(5000)
basic.forever(on_forever)
