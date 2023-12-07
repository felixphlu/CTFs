# Homelab

First I will run ifconfig to check my IP address on my Kali Linux machine

<figure><img src=".gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

I will also run ipconfig to check my IP address on my Windows machine

<figure><img src=".gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

As shown, the static IP address I set up for my Kali Linux machine is : 192.168.20.11

The IP address I set up for my Windows machine is: 192.168.20.10

On the Kali Linux machine, I will use nmap command to perform a scan of everything with "-A" and "Pn" to skip the pings targetting my windows machine.

<figure><img src=".gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

After the scan, we can see that port 3389 is currently open, that is RDP

<figure><img src=".gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

I want to create a basic malware now by using msfvenom and deploy it onto my Windows machine. I will not build malware to evade detections but instead to demonstrate telemetry as this malware would normally be detected by anti-virus.

I'll start building the malware using a meterpreter reverse shell as the payload.

To get a list of all the payloads, I ran the following:&#x20;

<figure><img src=".gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

I will use the following payload:&#x20;

<figure><img src=".gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

I left the default port from interpreter that is usually 4444. The following command will generate the malware using meterpreter's reverse TCP payload which is instructed to connect back to a machine based on the lhost (my kali linux or attacker machine) and lport. The file format will be an exe (executable) and the file will be named resume.pdf.exe

<figure><img src=".gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

As seen, the payload has been created.

<figure><img src=".gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

Now that I have the binary, I will open up a handler that will listen in on the port that I configured in the malware. I open Metasploit with msfconsole and use the multi-handler.

<figure><img src=".gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

I use options command to see what I can configure.

<figure><img src=".gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

Note that the highlighted payload option is set to generic/shell\_reverse\_tcp. I will change this payload so it is the same payload that I used when I configured the malware in msfvenom.

<figure><img src=".gitbook/assets/image (22).png" alt=""><figcaption><p>Updated the payload</p></figcaption></figure>

Now I want to change the lhost to my attacker machine. The lport is default 4444 which is what I had already set.

<figure><img src=".gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

To start this handler, I typed in exploit and now I am listening in and waiting for the test machine to execute the malware.

<figure><img src=".gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

I will now setup a quick HTTP server on my Kali machine so my test machine can download the malware. I can do this by using Python or startup and Apache service. I will use Python here and a port that is not being used (9999).

<figure><img src=".gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

Now onto my windows machine, I will first disable Defender.

<figure><img src=".gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

I will then access the internet browser and type in my ipf cali with port 9999 and download the Malware I created onto my windows machine.

<figure><img src=".gitbook/assets/image (30).png" alt=""><figcaption><p>We can see the resume.pdf.exe malware I created</p></figcaption></figure>

At a glance, the file looks like a PDF from my download folder.

<figure><img src=".gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

However, if I click on View > Details > Enable File name extensions, I can see that the file is an exe file and not a PDF.

<figure><img src=".gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

From the command prompt, I will use netstat to see if an established connection to my kali machine is there.

<figure><img src=".gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

In the task manager, I can also see the Resume executable

<figure><img src=".gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

Now switching over to my kali Linux machine and looking at my handler, we have an open shell.

<figure><img src=".gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

I will use shell

<figure><img src=".gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

I will use net user

<figure><img src=".gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

I will use net localgroup

<figure><img src=".gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

As well as ipconfig

<figure><img src=".gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

Now back to my Windows machine, I will use Splunk and create an index named endpoint that will ingest all my data/logs and centralize it.

<figure><img src=".gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

I also use the Sysmon addon to have the sysmon logs.

I query my search to filter only the logs from the attacker IP address.

<figure><img src=".gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

I can see that it is only targeted on destination port which is 3389 (RDP).

<figure><img src=".gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

If I were analyzing this, I would ask should this machine be attempting to connect to our RDP port? What machine is this or who does it belong to?&#x20;

Although, I cannot make sense that this was an nmap scan simply by looking at this telemetry which is why it is important to have a network sensor sitting in between our machines because we would not only see the potential signatures being generated and the ports that were scanned but we would also see the TCP flags if nmap was using TCP scans.

<figure><img src=".gitbook/assets/image (47).png" alt=""><figcaption><p>13 events from querying resume.pdf.exe</p></figcaption></figure>

13 Events are shown and 7 EventCodes were generated

<figure><img src=".gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

I will stick to EventCode #1 here.

<figure><img src=".gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

The parent process spawned cmd.exe with process\_id: 8308.

<figure><img src=".gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

I can use this ID to query the data to see what this command prompt had done by searching this ID using parent process\_id.

Instead, I will use process\_guid

<figure><img src=".gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

I will use it to search and I get 5 events.

<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

I can clean up the query:

<figure><img src=".gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

I can see here that our parent image resume.pdf.exe had spawned cmd.exe.

<figure><img src=".gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

In which eventually it had ran net user, net localgroup and ipconfig.

<figure><img src=".gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

From here, we can start creating detections so we can alert analysts next time a similar activity occurs in the future.
