import cv2 as cv
import os

def main():
	dir_name = input("Folder to convert >> ")
	art_files = os.listdir(dir_name)

	try:
		os.mkdir(dir_name + "_data")
	except:
		pass

	for file in art_files:
		img = cv.imread(dir_name + "/" + file)
		img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
		output = open(dir_name + "_data/" + file.split(".")[0] + ".txt", "w")
		for col in range(len(img)):
			for row in range(len(img[col])):
				output.write(str(img[col][row][0]) + "," + str(img[col][row][1]) + "," + str(img[col][row][2]) + "\n")
		output.close()
		print("Converted file: " + file)
main()