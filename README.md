# RGBMatrix
A completely remote customizable rgb matrix controlled by a raspberry pi zero w.

The screen is a 16x16 led rgb matrix that is individually addressable. It takes a pixel value data file from an image converted from the conversion script, and runs the art/animation on the pi. Everyting can be uploaded and run using SSH that requires setup before usage. This project can display still frames and animations.

- pixel conversion is run on .png files, outputs text files corresponding to the image.
- upload text files to a named folder on the pi that corresponds to name of the art piece.
- run the main script that loads and displays the image(s).
