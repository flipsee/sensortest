0.9 OLED 4 pin (GND,VDD,SCK,SDA)

Arduino:
- pin: (GND,VDD=5v,SCK=A5,SDA=A4)
Driver & Sample:
- https://github.com/adafruit/Adafruit_SSD1306
- https://github.com/adafruit/Adafruit-GFX-Library
- use the ssd1306_128x64_i2C.ino to test.
Note: use the i2c_scanner.ino to get the address and then replace it in the sketch above.
for this case is 0x3C (line 61)
display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3D (for the 128x64) 

- can also use the u8glib, but it only display on half of the screen, probably choose the wrong device need to explore more on this.
https://github.com/olikraus/u8glib/
