### UCLan Supercomputer facility  (HPC Wildcat)

#### Working on the cluster - some definitions
You may hear a supercomputer referred to as an HPC (High Powered Computing), a cluster or, in the case of the machine at UCLan, Wildcat. These all refer to the same thing. A cluster is a group of connected computers that can work together to perform tasks. Each computer on the cluster is called a *node*. Wildcat has 64 *compute nodes*, these are the machines that your jobs will run on. There is also a *head node* (some clusters have more than one). This is the node you will login to and submit your jobs. The head node on Wildcat is called **leopard**.
<br>
Just like a regular machine, each node has a number of cores. Each of the compute nodes on Wildcat has 8 cores and ~25Gb of memory.
<br>
I use the word 'job' to describe any code that you run on the computer, setting a simulation running is an example of a job.
#### Logging on to Wildcat
You will be using SSH to login to the supercomputer. To make the process a bit easier, you can add the following to your config file in ~./ssh, if that file is not present do not worry, you can just create it.

```bash
Host uclanhpc
    HostName 193.61.251.71
    User your_username
    Port 22

Host leopard
    HostName leopard
    User your_username
    Port 22
    ProxyCommand ssh -W %h:%p uclanhpc
```
This makes it easier to log in to the HPC. When you have made this change you will be able to type `ssh -XY your_username@leopard` and login to the leopard node of the HPC. It will ask you for your password twice, once to login to the 193.61.251.71 server (called **tiger**) and a second time to login to the head node called **leopard**. This is where you will submit your jobs.
<br>
<br>
When you login for the first time, your home area will be empty. Here you can create your own file structure to keep things organised. The file system on Wildcat has a maximum capacity of 44Tb and you can see your own disc usage with `du -sh`. Keep in mind that the space is not infinite, so if you can compress/remove any unwanted files or transfer them to starlink etc then feel free. It is unlikely that you will use huge amounts of storage but it is something to be aware of.

#### Modules
Working on the cluster is different from working on a regular laptop or PC. Instead of software being availible to you right away, it is controlled through *modules*. Let me show you an example:
![image](/Users/adamfenton/Documents/PhD/cheatSheets/hpc_manual/screenshots/modules.png)
In the screenshot above, you can see I use the command `module list` to show me which modules I currently have loaded (none at first). I then use `module avail` to show me which modules are availible on the cluster. I then use the `module load` command to load the `python/3.8.1` module. Using the `module list` command again shows me that python3 has been loaded.
<br>
<br>
![image](/Users/adamfenton/Documents/PhD/cheatSheets/hpc_manual/screenshots/load_module.png)
I am just illustrating the process here, you would not be loading python3 on the head node because **we do not run code on the headnode**. The head node is only for compiling and submitting jobs, which I will get on to shortly.
#### Bashrc file
If you are familiar with bash then you may know about the bashrc file already. If not, the bashrc file contains a list of commands that are executed every time you login. This saves you having to type the same things in every time! (Actually it is .bashrc, the dot means it is hidden and will not be listed when you type `ls`.) For example, my .bashrc file contains the following
```bash
export HDF5_DIR=/home/afenton/hdf5-gfortran
export LD_LIBRARY_PATH=/home/afenton/hdf5-gfortran/lib:$LD_LIBRARY_PATH
```
What these commands do is not important at the moment but because they are in my .basrc file, the *enviroment variable* `HDF5_DIR` is always set to `/home/afenton/hdf5-gfortran` and I don't need to set it every time I open a new terminal. You can also define aliases in here, for example:
```bash
alias c="clear"
```
I have the above alias set so, when I want a clean terminal, I don't have to type the full word, I just press c and hit return. <br>

Keep in mind that for any changes you make to the .bashrc file to work the first time, you need to reload it with `source .bashrc`. Note that you only need to do this immediately after making the changes, after that it will be done automatically when you login.


#### Submission of jobs
I mentioned before that we do not run code on the head node. I will use the SPH code PHANTOM as an example in the following. When logged on to the headnode using the process outlined above, you **cannot** just run the code as you normally would with `./phantom disc.in`. This will use up all the resources availible on the head node and stop all other users from submittion their own jobs. Instead you use a PBS script, see the example below, to request resources, give your job a name and load the appropriate modules. When you execute this script, your job will be submitted to the *scheduler* and, if the resources you requested are availible, your job will run.
![image](/Users/adamfenton/Documents/PhD/cheatSheets/hpc_manual/screenshots/submission.png)
Again using PHANTOM as an example, this script will be in the same directory as your `disc.in`, `disc_00000.tmp.h5` files (i.e. any files that the code requires to run, such as initial conditions).
#### Compiling code on Wildcat
The process of compiling code and installing dependancies (if they are not already installed as a **module**) is a bit nuanced and can require a little bit of fiddling. If you have any specific problems, let me know and I will give you a hand.


**Do not worry when you submit a job and you don't see anything on your screen. Jobs that you submit run 'in the background' and you do not see the usual output to terminal that you would see when running on a laptop or PC**


#### Addendum - running jobs interactively
As mentioned above, when running jobs on wildcat or any HPC, the standard output (stdout) of the code does not appear in terminal as it would if you were running it on your own machine. This can be irritating when trying to debug something as you will not see the error messages. One way, and perhaps the best way, of circumventing this is to use *bash redirection* to pipe the stdout to a file using something like `./phantom disc.in >> output.txt`. There is an option in the submission script to do this for you but I have known it to not work correctly and consistently and have found it better to do it myself.
<br>
In addition to this, to further aid debugging, you can run a job in **interactive mode**. To do this you use the `-I` flag in your `qsub` command, for example `qsub -I submitPhantom.pbs`. This will submit the job in interactive mode and you will be transfered to a terminal on a specific node (meaning you only have access to 8 cores). Here you will be able to run your code using the commands you would use if you were running on your own machine (for example `./phantom disc.in`). **NOTE:that you will have to reload any modules and change directory to your working directory**. To exit an interactive job, you use `exit`. It is rare that you will have to do this, but it can be helpful for debugging because the stdout is printed to screen and any error messages are readable. If you do want to do this, give me a shout and we will make sure you aren't inadvertently running code on the headnode.


<!-- Compiling PHANTOM on the cluster follows a similar process as it does when compiling it on a laptop or other PC but there are some important differences. Firstly, for the HDF5 file format to work, the HDF5 libraries need to be compiled using the same compiler as PHANTOM. In this case, we will use gfortran for both. Follow the steps below to compile HDF5 with gfortran:
1. Download the .tar file I have sent you, this contains the HDF5 libraries.
2. Copy the .tar file into your home area on the HPC using scp, for example <br>`scp hdf5-1.12.0.tar your_username@leopard:~/`.
3. Extract the files using `tar -xvf hdf5-1.12.0.tar` and move into the hdf5-1.12.0 directory.
4. Configure with `./configure --prefix=/path/to/hdf5/directory --enable-fortran --enable-cxx`
5. make and make install with `make` and, when that is finished, `make install`

When I did this, it took a while so be prepared for that. <br>
This is where the .bashrc file comes in useful. In order for PHANTOM to run, we need to tell it where to find the HDF5 libraries, we do that with the commands
```bash
export HDF5_DIR=/path/to/hdf5/directory
export LD_LIBRARY_PATH=/path/to/hdf5/directory/lib:$LD_LIBRARY_PATH
```
If you put these in your .bashrc file then they will be stored and you will not need to reset them each time.
<br>
<br>
Now we are ready to compile PHANTOM. Sometimes compiling on the headnode of Wildcat does not work, so before trying to compile you need to connect to another node called **gnode01** with `ssh gnode01`. It will ask for your password. Once you have logged in there, navigate to your run directory and generate your Makefile in the same way as you would on a laptop or PC. When you have your makefile you are ready to compile PHANTOM with
```bash
make HDF5=yes HDF5ROOT=$HDF5_DIR  SYSTEM=gfortran
```
When that compilation is complete, you should have the binary `phantom` in your directory. Now we can use our submission script to submit the job. In the following example, I assume your .in file is called `disc.in`. If it isn't then it will need changing in the submission script.
![image](/Users/adamfenton/Documents/PhD/cheatSheets/hpc_manual/screenshots/submission.png)
You will need a copy of this script in your *working* directory (the one where the `disc.in` file is). You can see at the top of the figure that I have named my script submitPhantom.pbs so to submit my job I will run the following command `qsub submitPhantom.pbs`. This will add your job to the queue and if the resources are available then the job will run. You can check its progress with `qstat -a` and `showq` (showq will show you all the jobs running on the cluster and also how many nodes are available.). -->


That is a very brief rundown on the cluster (and clusters in general). You may find it a bit tricky to get things going right away but any problems at all then come and find me.

If you are using the UCLan HPC then you have probably heard from Christian Kay. If you have any big problems then he is the guy to talk to!
