# autosplash.py
# ------------------------ #
# Used pexpect module to
# automatically answer all
# the SPLASH prompts
# Quick and dirty - can be
# improved with a function
# ------------------------ #
# Author: Adam Fenton
# Date: 20220907
# ------------------------ #

import pexpect
import glob
import subprocess

complete_file_list = glob.glob("run1*")
complete_file_list = sorted(complete_file_list, key = lambda x: x.split('.')[3])


def splash_interact_coodinate_plots(filename,PID,y_axis,x_axis,render,vector):
    ''' This function answers the splash command line prompts for a coodinate
        plot - specifically a coodinate plot (i.e. in x and y) because only these
        allow for particle rendering.
    '''
    savename = '%s.png' % filename
    # First 'spawn' to command i.e. splash <filename>. I am
    child = pexpect.spawn('/path/to/splash/executable/splash '+ filename)
    child.expect('') # Ask for option
    child.sendline('l3')
    child.expect('') # Ask for particleID
    child.sendline(PID)
    child.expect('') # Ask for xmin
    child.sendline('5')
    child.expect('') # Ask for xmax
    child.sendline('5')
    child.expect('') # Ask for ymin
    child.sendline('5')
    child.expect('') # Ask for ymax
    child.sendline('5')
    child.expect('') # Ask for zmin
    child.sendline('1.5')
    child.expect('') # Ask for zmax
    child.sendline('1.5')

    child.expect('') # Distance key (-- 1 AU --)
    child.sendline('g4')
    child.expect('')
    child.sendline('yes')
    child.expect('')
    child.sendline('1')
    child.expect('')
    child.sendline('1 AU')
    child.expect('')
    child.sendline('0.5')
    child.expect('')
    child.sendline('1.0')


    child.expect('') # Colourbar under plot
    child.sendline('r4')
    child.expect('')
    child.sendline('2')
    child.expect('')
    child.sendline('yes')

    child.expect('') # Colour of window
    child.sendline('p8')
    child.expect('')
    child.sendline('0')
    child.expect('')
    child.sendline('yes')
    child.expect('')
    child.sendline('1.00')
    child.expect('')
    child.sendline('7')

    child.expect('') # Size of window
    child.sendline('p3')
    child.expect('')
    child.sendline('3')
    child.expect('')
    child.sendline('no')

    child.expect('') # Axes options
    child.sendline('p2')
    child.expect('')
    child.sendline('-2')

    child.expect('') # Axes options
    child.sendline('p6')
    child.expect('')
    child.sendline('2')

    child.expect('') # Ask for option
    child.sendline('l5')
    child.expect('')
    child.sendline('6')
    child.expect('')
    child.sendline('1')
    child.expect('')
    child.sendline('0')


    child.expect('') # Ask for option
    child.sendline('l1')
    child.expect('')
    child.sendline('yes')
    child.expect('')
    child.sendline('no')
    child.expect('')
    child.sendline('no')

    child.expect('') # Ask for Y axis
    child.sendline(y_axis)
    child.expect('') # Ask for X axis
    child.sendline(x_axis)
    child.expect('') # Ask for render
    child.sendline(render)
    child.expect('') # Ask for vectory
    child.sendline(vector)
    child.expect('') # Ask for filename to save as
    child.sendline(savename)
    child.expect('') # Press q to quit
    child.sendline('q')

    child.interact()
for filename in complete_file_list:
    # print(filename)
    PID = filename.split(".")[2]
    subprocess.check_call('ls %s > splash.titles' % filename, shell=True)
    splash_interact_coodinate_plots(filename,PID,'2','1','6','0')
