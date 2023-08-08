from rpi_ws281x import *

def main():
    LED_COUNT = 256     
    LED_PIN = 18        
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 70
    LED_INVERT = False
    LED_CHANNEL = 0

    matrix = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,LED_CHANNEL)
    matrix.begin()
    matrix.show()
main()