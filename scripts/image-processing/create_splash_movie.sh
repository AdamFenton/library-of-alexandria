#!/bin/bash

# Creates a movie from the splash PNG files. Note that this can be modified to
# make a movie of any collection of plots as long as they are named sequentially
# and have padded zeros in the file name. In this case, the command has
# "splash_%04d.png" which means it is looking for files that start with `splash_`
# and end with a digit padded out to 4 zeros. This means that 1 becomes 0001, 10
# becomes 0010 etc. You can define this naming convention in python quite easily
# with string formatting

ffmpeg \
 -framerate 10 -f image2\
 -i "splash_%04d.png" -q:v 2 -c:v mpeg4 -r 24
 -vf scale=1920:-1 -pix_fmt yuv420p  output.mp4
