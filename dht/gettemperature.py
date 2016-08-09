#Tutorial : http://osoyoo.com/?p=858
import datetime
import time
import dht11
import RPi.GPIO as GPIO

# Define GPIO
Temp_sensor=5

def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  instance = dht11.DHT11(pin = Temp_sensor)

  try:  
    while True:
        #get DHT11 sensor value
        result = instance.read()
        reading_time = datetime.datetime.now()
        
        # Send some test
        if result.is_valid():
            print("time:"+str(reading_time))
            print("temp:"+str(result.temperature) + " C")
            print("humid:"+str(result.humidity)+ "%")
            time.sleep(5) # 5 second delay
  finally:
    print("Reading End.")

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()

