---
title: "Mr. Robot - TryHackMe CTF Writeup"
source: "https://medium.com/@aycagl/mr-robot-tryhackme-ctf-writeup-b8f30bb3cdf9"
tags:
  - "clippings"
---
## Key 1:

We begin with an initial nmap scan. Here, we use the -sV parameter to retrieve version information, -sC parameter to obtain script details, and -T4 parameter for faster scanning.

![](https://miro.medium.com/v2/resize:fit:875/1*_3EnGw3tMX4yD843Evizhw.png)

Based on the scan results, we discover 3 ports. Port 22 for SSH is closed, while ports 80 and 443 are open. Let’s examine the website.

![](https://miro.medium.com/v2/resize:fit:875/1*OkBs5EV66Zauk-KnTGvRBg.png)

When we visit the website, we encounter some text and commands we can use. Running these commands, we find videos and other content but nothing particularly useful. To discover subdirectories, let’s use the gobuster tool.

![](https://miro.medium.com/v2/resize:fit:875/1*cEDG9mPXaWYxKBcuoRrA8w.png)

![](https://miro.medium.com/v2/resize:fit:875/1*FXA4KfiKhCwKCpLjRvajsw.png)

The gobuster results reveal many subdirectories, but most of them do not contain valuable information. Let’s navigate to the /readme subdirectory.

![](https://miro.medium.com/v2/resize:fit:813/1*uKNrQO5-e_rX6lk5-70rGA.png)

Even here, we don’t find any useful information. Let’s proceed to the /robots.txt subdirectory.

![](https://miro.medium.com/v2/resize:fit:724/1*pzxus9NnKh3ZwbsIzrq13w.png)

Here, we find the first key and a dictionary. Let’s start by obtaining the key.

![](https://miro.medium.com/v2/resize:fit:729/1*e8SdkQl2ofUMcSMTz71Emw.png)

## Key 2

By using the command “/fsocity.dic,” we download the dictionary file to our machine, which we’ll use shortly.

![](https://miro.medium.com/v2/resize:fit:875/1*yc-TVdfs74TDlK4pxn2EKA.png)

When we go to the /wp-login directory that came from the Gobuster results, we encounter the WordPress login screen. We can log in using the dictionary information we obtained.

![](https://miro.medium.com/v2/resize:fit:875/1*yRZAkvxRN8og8Y-gQKZn8g.png)

When we explore the dictionary, we notice some repeated words, which might slow down our search. We can use the “wc” command to check the total line count and use “sort -u” to remove duplicates, saving the output to a file named mrrobot.

![](https://miro.medium.com/v2/resize:fit:481/1*upCvErvOHwhq-HyP7TgDsw.png)

When attempting random logins on the login screen, we receive an “Invalid username” error. This error message can be a security vulnerability that we can exploit using the BurpSuite tool. Our goal is to capture traffic while making login attempts and try to crack the password using the information it contains.

![](https://miro.medium.com/v2/resize:fit:564/1*EsJ_rToGG8w8NiNFOSaU9Q.png)

First, let’s open the BurpSuite tool. I’m using the FoxyProxy extension to capture traffic from my browser in BurpSuite. You can use FoxyProxy for both Chrome and Firefox. Once FoxyProxy is activated, I turn on “intercept” in the BurpSuite tool.

![](https://miro.medium.com/v2/resize:fit:875/1*GmhRwXu_EBrGiwwXv25_VA.png)

By attempting a random username (admin) and password (admin) on the login screen, we capture the traffic with BurpSuite. The line indicated in Figure 15 is relevant to this. We copy this information.

![](https://miro.medium.com/v2/resize:fit:875/1*pROMjCn92ol5dkZ6Jc9QBw.png)

Now, let’s use the Hydra tool to perform password cracking. The following command will help:

![](https://miro.medium.com/v2/resize:fit:875/1*Kzp6FoEtZ4kMl3j1pnca7g.png)

In the first step, we need to obtain the username. We use -L for the username list and -p for a random password. Since we are using the Hydra tool with the http-post-form module, we specify this. We enclose the page we want to attempt, which is /wp-login.php, and the copied part from the BurpSuite tool in double quotes. We update the user field as ^USER^, and at the end, we specify the error we received, “Invalid username,” and run the command.

We have obtained the username!

![](https://miro.medium.com/v2/resize:fit:845/1*WhWDzh226lZVPn-lwhST4Q.png)

When we enter the username, we encounter a different error related to the password. This time, we will use the Hydra tool to find the password.

![](https://miro.medium.com/v2/resize:fit:531/1*3u8QcFr9dMTyk6PBl3yQnw.png)

Since we now know the username, we use the -l parameter for the username and -P parameter for the mrrobot file as the password list. We specify ^PASS^ for the password field, Elliot for the log field, and the last part, “The password…,” for the error we received. Running the command, we obtain the password.

![](https://miro.medium.com/v2/resize:fit:875/1*T6Yx3yxEeypwTFWT2PLldg.png)

With the obtained information, we log into the system. Upon exploring the system, we discover that we can make edits in the “Editor” section under “Appearance.” Here, we can replace the relevant code with our own code to obtain a reverse shell.

![](https://miro.medium.com/v2/resize:fit:875/1*81fx_wUA089P85mMVUl_hQ.png)

![](https://miro.medium.com/v2/resize:fit:875/1*HU8v_R3ZkXEYU_LFKS3_7A.png)

Let’s use the [pentestmonkey](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) code for this.

![](https://miro.medium.com/v2/resize:fit:875/1*SisB2C0S-3gJnv5as6nACg.png)

In the pentestmonkey code, we replace $ip with our local IP address. We can leave the port section as is. We prefer to upload the code to the “archive.php” page, but it can also be uploaded to the “404.php” section. After making the necessary changes, we save the code.

![](https://miro.medium.com/v2/resize:fit:875/1*QBX0JnU8tWwZ4_5NF33Y8g.png)

Next, we open a netcat listener in our terminal. By visiting [http://10.10.234.108/wp-content/themes/twentyfifteen/archive.php](http://10.10.234.108/wp-content/themes/twentyfifteen/archive.php), we execute the reverse shell code and gain access to the system. (Here, the IP part is the machine’s IP address.)

![](https://miro.medium.com/v2/resize:fit:875/1*ez22T6Uc3nXjqhjgNzRaXw.png)

We have logged into the system as the daemon user. Under the /home directory, we see that there are 2 files for the robot user.

![](https://miro.medium.com/v2/resize:fit:218/1*sMUKWA3Wj9ZzgsjOUtW85w.png)

We cannot open the file containing the second key. We need to switch to the robot user.

![](https://miro.medium.com/v2/resize:fit:456/1*47SasML0gVVNKbFWEIO_dA.png)

Inside the “password.raw-md5” file, we find the MD5 encrypted password for the robot user. Let’s crack it using [Crackstation](https://crackstation.net/).

![](https://miro.medium.com/v2/resize:fit:875/1*K-6bZvIKh3u-k0BQgeIuHA.png)

We have obtained the password for the robot user. When we attempt to switch users, we encounter an error since we are not in the terminal.

![](https://miro.medium.com/v2/resize:fit:389/1*ZOmXLz30WB2XQZElYJsp4w.png)

We need to transition from the shell to the terminal. To do this, we use the Python command found on the [ropnop blog](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/).

![](https://miro.medium.com/v2/resize:fit:875/1*iTLgzlr9XzVtOjVWWS0W1w.png)

Finally, we switch to the robot user and obtain the second key!

![](https://miro.medium.com/v2/resize:fit:554/1*u8loXju55CAywrgoaHQ-zw.png)

## Key 3:

We are in the process of elevating privileges for the last key. I check if I can run a file with sudo privileges using “sudo -l,” but I find that I can’t.

![](https://miro.medium.com/v2/resize:fit:644/1*cCU_Iw8FTouemeIm7sOEeA.png)

We can find SUID files to escalate to the root user. To find SUID files, we use the relevant command in the terminal. (The “2>/dev/null” part is used to avoid error messages.)

![](https://miro.medium.com/v2/resize:fit:629/1*Ef2GPJbAbhXAr2eFQ3ZDcg.png)

When we examine the SUID files we found on the [Gtfobins](https://gtfobins.github.io/gtfobins/nmap/) page, we realize that we can use nmap to our advantage.

![](https://miro.medium.com/v2/resize:fit:875/1*DceDsxJyqxCmKR_NnLWExQ.png)

With the nmap SUID file, we can run the nmap tool with root privileges. We transition to the nmap interface by typing “nmap — interactive” in our terminal. Using the “!sh” command, we obtain a shell. And ultimately, we have root access!

![](https://miro.medium.com/v2/resize:fit:658/1*Zy1lCTgX1AMxHE79WdMywA.png)

Under the /root directory, we find our third key!

![](https://miro.medium.com/v2/resize:fit:875/1*7FkgGXI6-4CHIaWtsjMBhQ.png)

Thank you for reading. See you in the next solutions!