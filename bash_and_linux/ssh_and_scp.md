### Remote Access
---
#### SSH Config File
---
If you have ssh'd to a server at all before, then you will have a **hidden** folder in your home directory called `.ssh`. To see it from the command line you can use the `-a` flag when using `ls`. This directory contains everything you need when tinkering with your ssh. Most importantly, there may be a file called `config` but if there is not one there, you can safely create it with `touch config` from inside the `.ssh` directory.
<br>
The ssh config file allows you to set up connections to your remote machines so you don't have to type the full address every time. This is particularly useful with a system like the university one in which you need to go through stargate before accessing your personal machine.
<br>
**I cannot include my ssh config file for security reasons but I have written a fake one below to give an understanding of how they work**

```
  Host HOSTA
    HostName HOSTA.address.foo.bar
    User user1
    Port 1111
    IdentityFile ~/.ssh/id_rsa_HOSTA
    ForwardX11 yes
    ForwardX11Trusted yes
    XAuthLocation /opt/X11/bin/xauth

Host HOSTB
    HostName HOSTB
    User user1
    Port 1111
    ProxyCommand ssh -W %h:%p HOSTA
    ForwardX11 yes
    ForwardX11Trusted yes
    XAuthLocation /opt/X11/bin/xauth

```
So say I have a host, HOSTB, that I would normally access by first going through HOSTA (by first `ssh user1@HOSTA` and then, when logged in, `ssh user1@HOSTB`). We can use the ssh config file to make that more efficient. The above code snippet first defines HOSTA your username, the port number, and Identity File which is used for ssh keys (gets a bit complicated here but read around it, plenty of stuff online) and then the two final lines automatically use X forwarding so you dont need the -XY flag when you ssh.

The second entry, HOSTB, uses a proxy command that first ssh's into HOSTA and then into HOSTB. When you have this set up, all you have to type at the command line is `ssh HOSTB` and, once you enter your passwords, you will be in HOSTB
