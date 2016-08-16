8x8 Led Matrix with the Max7219 controller chip
3-5v

Datasheet: http://pdfserv.maxim-ic.com/en/ds/MAX7219-MAX7221.pdf

Arduino:
- Pin: 5pin (VCC=5v, GND, DIN=D12, CS=D10, CLK=D11)
- Driver: LedControlMS.zip
- Sample: MakeSpace_LEDMatrix.ino in the zip above.

ESP8266:
- Pin: 5pin (VCC=3v, GND, DIN=D5/GPIO14, CS=D6/GPIO12, CLK=D7/GPIO13)
- Driver: same with arduino above
- Sample: same with the arduino sample but change the line#12 to LedControl lc=LedControl(14,13,12,1);

RaspberryPI:Not Tested

----- Source -----
- http://www.instructables.com/id/LED-Matrix-with-Arduino/?ALLSTEPS
- http://playground.arduino.cc/Main/LedControl
