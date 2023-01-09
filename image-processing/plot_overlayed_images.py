# plot_overlayed_images.py
# ------------------------ #
# Takes a list of background
# and forground images and
# overlays the forground over
# the background and making it
# semi transparent. See the
# example in the examples/
# directory
# ------------------------ #
# Author: Adam Fenton
# Date: 20230107
# ------------------------ #
from PIL import Image
import glob


# Find all images matching the pattern and make sure they are sorted (using
# the lambda function here so that the order is disc_00001 disc_00002 disc_00003
# etc)
bg_images = sorted(glob.glob("full_disc/*"), key = lambda x: x.split('_')[2])
frag_images = sorted(glob.glob('F4/*'),key = lambda x: x.split('_')[1])


# Loop through the image lists
for b,f in zip(bg_images,frag_images):

    idx = f.split('_')[1].split('.')[0]

    background = Image.open(b)
    overlay = Image.open(f)


    # Convert the colour pallette from RGB to RGBA (A for alpha) which allows
    # us to change the opacity (alpha = 1 (opaque), alpha = 0.1 (very transparent))
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    # Overlay the two images with alpha = 0.5
    new_img = Image.blend(background, overlay, 0.5)
    # Save new image
    new_img.save("F4/F4_%s.png" % idx,"PNG")
