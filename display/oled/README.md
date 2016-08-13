0.9 OLED (SSD1306): 4 pin (GND,VDD,SCK,SDA) 

Note: 
- use the i2c_scanner.ino to get the address and then replace it in the test sketch.
- this display doesn't auto clear the display, when program is terminated, it still display the last content on the screen freezing until the VCC pin is plugged out. remember to clear screen on program termination!

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
- pin: (GND,VDD=3v,SCK=GPIO3\SCL,SDA=GPIO2\SDA)
- Driver: https://github.com/adafruit/Adafruit_Python_SSD1306.git
- Sample: included in the driver above.

----- Sources -----
- http://arduino-er.blogspot.sg/2016/04/nodemcu-esp8266-to-display-on-128x64.html
- https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/usage
