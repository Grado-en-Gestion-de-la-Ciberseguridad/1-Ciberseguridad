---
title: "TryHackMe WalkThrough — Mr Robot CTF"
source: "https://medium.com/azkrath/tryhackme-walkthrough-mr-robot-ctf-9e9eecd2036"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:875/1*KNO93RtHJlic6nbR8yyWlQ.jpeg)
## Enumeration

Let’s start with a basic Nmap scan and a check on the main site:

![](https://miro.medium.com/v2/resize:fit:875/1*CPzOwTaBHUK-9wolL8fIeQ.png)

Nmap scan

We can see that we have just 2 open ports on this machine:

- Port 22 — SSH is closed
- Port 80, 443 — A web page running a search website

By checking the main site, we are presented with a small intro and then a set of options to choose:

![](https://miro.medium.com/v2/resize:fit:875/1*I4B6keL6UKGBpn7M-P-I0Q.png)

Main web page

Checking some of the commands, we are redirected to a bunch of videos and information of Mr. Robot show but nothing useful:

![](https://miro.medium.com/v2/resize:fit:875/1*fSyiWJvv0CJRydK9vE7TbA.png)

Checking different options

Our gobuster search also retrieved several directories, some of them related to Wordpress:

![](https://miro.medium.com/v2/resize:fit:875/1*cg0kfPEf82TwBpcvcsEbOA.png)

Gobuster directory search

After checking on some of those directories, we found the first flag at robots:

![](https://miro.medium.com/v2/resize:fit:875/1*vumSs1gEIiZgdtLOoZREtA.png)

First flag found at the /robots

We can now answer to the question “What is key 1?” with this first flag. We also get some kind of list with potential usernames and passwords, named ‘fsocity.dic’.

Continuing our search for the directories we found some base64 string in the license directory:

![](https://miro.medium.com/v2/resize:fit:875/1*iiPxaAf0EFDYhqBYsb2CDA.png)

Finding a base64 string in the license page

Let’s use [CyberChef](https://gchq.github.io/CyberChef/) to decode the string:

![](https://miro.medium.com/v2/resize:fit:875/1*I6-WJX3dRrTVLqwyI7ZYoA.png)

Using CyberChef to decode the base64 string

And we get a pair of credentials that might be useful somewhere. We also saw a bunch of Wordpress directories, so let’s head to the login page:

![](https://miro.medium.com/v2/resize:fit:875/1*w8ytxl85rcAsj5J9R-i-FQ.png)

Wordpress login page

Ok, let’s try these credentials and see if they are valid:

![](https://miro.medium.com/v2/resize:fit:875/1*aKtVrE76RXSVPvsiXyhEOA.png)

We are in as the user Elliot

And we are in! So now we can try to set up a reverse shell and get our first foothold on the server. Let’s get our reverse shell from [pentestmonkey](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) and set it up on the 404.php template:

![](https://miro.medium.com/v2/resize:fit:875/1*upHY15atdlyeWDip6610Sg.png)

Reverse shell in the 404.php template

After this, let’s set up a netcat listener on the Port defined above:

![](https://miro.medium.com/v2/resize:fit:875/1*pLpMve-bxsp2k2VYD0q2Yg.png)

Netcat listener

Let’s head to the template location using the following URL on the browser:

```
http://10.10.127.168/wp-includes/themes/TwentyFifteen/404.php
```

And we should get our shell on our machine:

![](https://miro.medium.com/v2/resize:fit:875/1*K-oern_iEC1mLIKYtOOL5Q.png)

We get a shell

Ok, so let’s see who we are and what is our currently working directory:

![](https://miro.medium.com/v2/resize:fit:875/1*_-3YJlKooeSrofXdTBtjYA.png)

User and currently working directory

Ok, we are the daemon user and we are at the root. Let’s check the /home directory and see if we have some permissions to do something:

![](https://miro.medium.com/v2/resize:fit:875/1*st11IxKg5l5rQ2xHsqXPiA.png)

Second flag found at /home/robot

Awesome! We can now answer to the question “What is key 2?” with this second flag.

## Privilege Escalation

So my usual steps into enumerate linux boxes usually are to check for sudo permissions, crontab jobs running and to get a linpeas script and run an automated enumeration in order to look for clues.

Since we have a dumb shell, we need to upgrade it to a interactive tty shell, using the following Python command:

```
python -c ‘import pty;pty.spawn(“/bin/bash”)’
```

We can check for the sudo permissions with the sudo -l command:

![](https://miro.medium.com/v2/resize:fit:875/1*RA6rePV2BdWmzgy-ocZINg.png)

Checking for sudo permissions

So we don’t have permissions to check if we can run something as sudo. Let’s check this password file that it is in the robot directory:

![](https://miro.medium.com/v2/resize:fit:875/1*S0WfWqGnSO313k3zHxC1VQ.png)

Checking the password hash file

We can see that it is a password hash file using md5, so let’s start John and break this thing:

![](https://miro.medium.com/v2/resize:fit:875/1*-V6582IDiysDk2zGOvgR4w.png)

Cracking the hash with John

After a couple of seconds, we got ourselves a new set of credentials:

```
username: robotpassword: abcdefghijklmnopqrstuvwxyz
```

Checking crontab, there is no jobs running so my next step usually is just to drop a linpeas script and check for some clues. Let’s start a Python web server on our script location:

![](https://miro.medium.com/v2/resize:fit:875/1*OPl2X8pNJ24C7o45jAMG1g.png)

Python web server up

And download the script into the machine:

![](https://miro.medium.com/v2/resize:fit:875/1*1JSfTjlBDSioEnrjV1cQkA.png)

Download linpeas script on the machine

After that, I’ve tried to run the script but for some reason I kept loosing my shell so I’m gonna leave it for now.

Since we can’t run ‘sudo -l’, maybe we can try to find some SUID binaries lying around. Let’s use the following command:

```
find / -perm -4000 2>/dev/null
```

And we get a couple of potential attack vectors right here:

![](https://miro.medium.com/v2/resize:fit:875/1*aWifC7diiqNl2grGFLv5Yw.png)

Finding SUID binaries

Ok, so checking [gftobins](https://gtfobins.github.io/gtfobins/) for those binaries, we can find Nmap with a potencial way of breaking of the restricted environment:

![](https://miro.medium.com/v2/resize:fit:875/1*FVtbmi3QPOkYvticlx-SMg.png)

Entry for Nmap at gtfobins

Ok, so let’s try the option b), by starting an interactive session on Nmap and trying to execute a shell:

![](https://miro.medium.com/v2/resize:fit:875/1*CHP3oFUBFUVm8hB-ENfl2A.png)

Exploiting nmap

Awesome! We are not root! So heading to the ‘/root’ directory, we should find our third flag:

![](https://miro.medium.com/v2/resize:fit:875/1*1Tsllpj8naZ2C31i_RvEkA.png)

Third flag found in /root directory

We can now answer to the question “What is key 3?” with the third and last flag.

This room as super cool for me, specially because I am a huge fan of Mr. Robot show and the videos and pages tell some sort of story. Also the enumeration phase was really cool, specially because there are multiple vectores of getting the initial foothold.

I hope you enjoyed reading this post as much as I enjoyed writing it. Let me know in the comments if something is wrong or missing, as I am still learning myself and feedback is always welcomed :)