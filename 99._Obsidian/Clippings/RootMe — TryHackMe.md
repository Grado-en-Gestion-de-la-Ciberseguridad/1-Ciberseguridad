---
title: "RootMe — TryHackMe"
source: "https://medium.com/@aycagl/rootme-tryhackme-cde75b7fd37a"
tags:
  - "clippings"
---
**Reconnaissance**

First, we perform nmap scan to find out which ports are open on the system.

![](https://miro.medium.com/v2/resize:fit:875/1*jRUHlvYb5vbg175zc5S-PQ.jpeg)

According to the scan results, 2 ports are open: port 22 for SSH and port 80 for HTTP. When we enter the relevant URL address into the browser, a web page appears.

![](https://miro.medium.com/v2/resize:fit:875/1*ktOxDr638_HeiOc1lDMBnw.jpeg)

We cannot find much information on the web page. When we right-click and view the page source, we still cannot obtain any information.

![](https://miro.medium.com/v2/resize:fit:866/1*-WAv-5K3Q4ssp_brvrU_qg.jpeg)

There may be other directories on the web page. We perform a scan on the web page using **Gobuster**. Let’s examine the results.

![](https://miro.medium.com/v2/resize:fit:875/1*M6H1D6jvknvcIxlz8nOsvQ.jpeg)

When we go to /js/, we cannot find any useful information.

![](https://miro.medium.com/v2/resize:fit:828/1*muuqUywOjB8RrVVZVoaoBA.jpeg)

In the /panel/ section, we find a file upload area. One idea: We can hack the system by uploading a malicious file from here!

![](https://miro.medium.com/v2/resize:fit:875/1*vyOEmWe25yKA3rrlABa3LQ.jpeg)

/uploads/ section will show what we have uploaded to the panel.

![](https://miro.medium.com/v2/resize:fit:746/1*0TSwnAzGHSVTs2KRVbGPOA.jpeg)

**Getting a shell**

We will obtain a reverse shell by uploading a malicious file to the /panel/ section. First, we will attempt to enter using the commonly used PHP scripting language for a reverse shell. For this, we can use the code provided on the GitHub page below:

We create a file named php\_reverse\_shell on our local system and save the code. We modify the $ip and $port sections. Since our computer will be the listener in the reverse shell connection, we write our VPN ip address in the ip section. We can leave the port section as 1234.

![](https://miro.medium.com/v2/resize:fit:793/1*9ZJU8BXO93BKKVDVg3T-Vg.jpeg)

Then, when we try to upload the PHP file to the /panel/ section, we see that the file upload is not allowed.

![](https://miro.medium.com/v2/resize:fit:875/1*fXBOP1szEpeOpLDJl-PMNg.jpeg)

We can try to upload it by changing the file extension. After a little research, we can access some examples of PHP file extensions. I prefer to use .php5 extension.

![](https://miro.medium.com/v2/resize:fit:386/1*2lu__P2iD6jPXM59LPXYQw.jpeg)

We upload our file to the system.

![](https://miro.medium.com/v2/resize:fit:875/1*JvDkTXgjCHfl3e0zucv--A.jpeg)

We can see our file in the /uploads/ section. Before clicking on the file, we need to establish a **netcat** connection in our own terminal to receive the reverse shell connection.

![](https://miro.medium.com/v2/resize:fit:875/1*yy9RDvRfBoHOMW5uy4zQdA.jpeg)

Netcat is used as a tool to enable us to listen. We enter the command:

*nc -lvnp 1234*

Then, we click on the file in the /uploads/ section and see that we have received a reverse shell in our terminal. We are now in the system!

![](https://miro.medium.com/v2/resize:fit:875/1*ibaWiXKqn6uhPJc8TIKIaw.jpeg)

To obtain a more stable shell, we write the following code:

![](https://miro.medium.com/v2/resize:fit:651/1*NfIevNwmHJKCMgVDXNXGzQ.jpeg)

To find the “user.txt” file we are looking for: We write the command:

*find / -type f -name user.txt 2>/dev/null*

The find command is used for searching. The 2>/dev/null part prevents errors from being displayed on the screen, making it easier to read.

![](https://miro.medium.com/v2/resize:fit:586/1*38qIPdlIGpKU8zEMIAnWgA.jpeg)

We found the relevant file. When we enter it, we obtain user.txt!

![](https://miro.medium.com/v2/resize:fit:278/1*WLY1rzLcQuj_JPhhXIFPKQ.jpeg)