## Visualisation of SPH datafiles uses SPLASH

### 1 - Overview
Splash is a command line tool developed by Daniel Price to visualise data from SPH
numerical hydrodynamics codes. It has very good documentation available at [https://splash-viz.readthedocs.io/en/latest/](https://splash-viz.readthedocs.io/en/latest/).
Since it is written by the same author(s) as the SPH code PHANTOM, it integrates very nicely. I recommend reading some of the paper for it to gain a surface level understanding of how it works.

### 1.1 - Further Details
Since the documentation for SPLASH is particularly good, I wont bother outlining everything here. Instead, I will make a note of some of the quick tips and tricks that I have made a regular part of my workflow that, though they are included, are a bit hard to find in the full documentation.

### 2 - Automation
SPLASH doesn't really have an API as such but, since it is a command line tool, we can use the python module `pexpect` to anticipate and answer the command line prompts. In this repository, under `/scripts/splash` there is a python script I have written that automatically answers all the prompts. This can be used in a bash for loop to loop through all datafiles in a directory and produce plots for all of them, without you having to answer all the prompts for each datafile!

Obviously you can fork/clone this repository and play around with the script for your own purposes.

### 3 - Making movies
The older versions of SPLASH and I believe in the version you have if you compiled from source come with a script called movie.sh. If you for some reason do not have or cannot find that script, the following is a one-liner I wrote which does the same thing. Note that you need to have the `ffmpeg` tool installed - I think it is installed on all the starlink machines, if you are working on a cluster then you will have to load the module first, (check module avail to see what it is called and then load with `module load <name>`.)

`ffmpeg -framerate 10 -f image2 -i "splash_%04d.png" -q:v 2 -c:v mpeg4 -r 24 -vf scale=1920:-1 -pix_fmt yuv420p  output.mp4`

The command above takes all the files that match the naming pattern `splash_0000.png, splash_0001.png, splash_0002.png, ...,` and creates a movie called output.mp4. The syntax for ffmpeg can get a bit confusing but there is decent documentation and plenty of answers on stack overflow to help.

I have added this and a couple more bash commands that use ffmpeg in the `/scripts/ffmpeg` directory that do other useful things. 
