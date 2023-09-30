import RPi.GPIO as GPIO
import time

# Set GPIO mode and define sensor pin
GPIO.setmode(GPIO.BCM)
sensor_pin = 18

def read_water_level():
    GPIO.setup(sensor_pin, GPIO.OUT)
    GPIO.output(sensor_pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(sensor_pin, GPIO.IN)
    while GPIO.input(sensor_pin) == GPIO.LOW:
        pass

    start_time = time.time()
    while GPIO.input(sensor_pin) == GPIO.HIGH:
        pass
    end_time = time.time()

    return end_time - start_time

try:
    while True:
        water_level_time = read_water_level()
        water_level_percentage = round(water_level_time * 100 / 5, 2)  # Assuming 5 seconds to fill the container

        print(f"Water level: {water_level_percentage}%")

        if water_level_percentage > 70:
            print("High Water Level Detected! Take Action.")
        elif water_level_percentage > 30:
            print("Moderate Water Level Detected.")
        else:
            print("Low Water Level Detected.")

        time.sleep(2)  # Adjust as needed for the desired reading frequency

except KeyboardInterrupt:
    GPIO.cleanup()
