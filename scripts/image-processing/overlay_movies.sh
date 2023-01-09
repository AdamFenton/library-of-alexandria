#!/bin/bash

# Same sort of thing as plot_overlayed_images.py but does it for two movies. The
# final movie is saved as overlay_output.mp4.

# The alpha value (opacity amount) is set by the colorchannelmixer=aa=0.5
# parameter

# master_movie.mp4 in the examples/ directory is an example of how this script
# works. The grey and coloured parts are two different movies I have overlayed.


ffmpeg \
    -i forground.mp4 -i background.mp4 \
    -filter_complex " \
        [0:v]setpts=PTS-STARTPTS, scale=1920x1080[top]; \
        [1:v]setpts=PTS-STARTPTS, scale=1920x1080, \
             format=yuva420p,colorchannelmixer=aa=0.5[bottom]; \
        [top][bottom]overlay=shortest=1" \
    -acodec libvo_aacenc -vcodec libx264 overlay_output.mp4
