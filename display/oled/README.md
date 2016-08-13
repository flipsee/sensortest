0.9 OLED 4 pin (GND,VDD,SCK,SDA)

Note: use the i2c_scanner.ino to get the address and then replace it in the test sketch.

Arduino:
- pin: (GND,VDD=5v,SCK=A5,SDA=A4)
- Driver:
  - https://github.com/adafruit/Adafruit_SSD1306
  - https://github.com/adafruit/Adafruit-GFX-Library
  - ???can also use the u8glib, but it only display on half of the screen, probably choose the wrong device. Need to explore more on this. https://github.com/olikraus/u8glib/
- Sample: ssd1306_128x64_i2c_ArduinoUnoR3.ino (modified from the Adafruit sample sketch)

ESp8266(arduino firmware):
- pin: (GND,VDD=3v,SCK=D1,SDA=D2)
- Driver: Same with the Arduino above.
- Sample: ssd1306_128x64_i2c_ESP8266.ino (modified from the Adafruit sample sketch)

RaspberryPI:
- pin: (GND,VDD=??,SCK=??,SDA=??)
- Sample: ??? 

----- Sources -----
- http://arduino-er.blogspot.sg/2016/04/nodemcu-esp8266-to-display-on-128x64.html
