from rpi_ws281x import *
import time
import os

LED_COUNT = 256
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = int(input("brightness: "))
LED_INVERT = False
LED_CHANNEL = 0

matrix = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,LED_CHANNEL)
matrix.begin()

def main():
    display_type = input("multi frames?: ")
    art_name = input("art name >> ")
    if display_type == "no":
        display_info(art_name)
        map2matrix(art_name + ".txt")
    else:
        speed = input("animation speed (seconds): ")
        display_info(art_name)
        frames_dir = os.listdir("data_files/" + art_name)
        while True:
            for frame in range(len(frames_dir)):
                map2matrix(art_name + "/" + str(frame) + ".txt")
                time.sleep(float(speed))

def map2matrix(name):
    try:
        file = open("data_files/" + name, "r")
    except:
        print("invalid file")
        os._exit(1)

    values = file.readlines()
    file.close()

    even_seg = 1
    px_line_cnt = 0
    matrix_px_cnt = 255
    incrementer = 1

    while px_line_cnt < LED_COUNT - 1:
        if even_seg > 0:
            incrementer = 1
        else:
            matrix_px_cnt -= 15
            incrementer = -1
        for x in range(16):
            val = values[px_line_cnt].strip("\n").split(",")
            matrix.setPixelColor(matrix_px_cnt, Color(int(val[0]),int(val[1]),int(val[2])))
            matrix_px_cnt -= incrementer
            px_line_cnt += 1
        if even_seg < 0:
            matrix_px_cnt -= 17
        even_seg *= -1
    matrix.show()

def display_info(art_name):
    print("==============================")
    print("    CURRENTLY DISPLAYING")
    print("        " + art_name)
    print()
    print("   epic program created by nhat")
    print("==============================")


main()
