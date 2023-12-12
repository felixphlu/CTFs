---
description: Splunk, Virustotal, Threatcrowd
---

# CD BOTS Lab Scenario 1 (APT)

This hands on lab will be an APT scenario to begin. In the scenario, reports come in that a group called "Po01s0n1vy" targetting the Wayne Enterprises. My goal is to investigate the attack with the Lockheed Martin Kill Chain.

<figure><img src=".gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

First, I will look at a graph to see when there was activity. I piped timechart count by src\_ip.

<figure><img src=".gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

I can see that an unknown IP address has been active on Wed, Aug 10th, 2016.

<figure><img src=".gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

I query my search for that IP address and find that they the web vulnerability scanner used by the APT is Acunetix. The website they are attacking is using Joomla as their content management system.

<figure><img src=".gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

I am searching for any posted files to find the name of the file that defaced the website.

<figure><img src=".gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

I could not find it with that query but then I find out that a different IP address was used to deface the website: poisonivy-is-coming-for-you-batman.jpeg and the FQDN (Fully Qualified Domain Name) associated with the attack is: prankglassinebracket.jumpingcrab.com. The other IP address used to attack the website is : 23.22.63.114 and they were using brute force password attacks.

<figure><img src=".gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

Next, I used Virustotal to check the IP address of the attacker

<figure><img src=".gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

I see AlienVault as the top search, so I decide to use threatcrowd as well

<figure><img src=".gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

Here, I used Virustotal and Threatcrowd. However, I could use other OSINT tools such as: Recordedfuture, lookingglass, cisco talos, Fire Eye, Mandiant and Mandiant Advantage.

I found the email operated by the APT group here: lillian.rose@po1s0n1vy.com.

<figure><img src=".gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

Next, I want to look for the executable uploaded by the attacker.

The attack date was 8/10/2016 from 21:00 - 22:00

<figure><img src=".gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

I query the search to sysmon logs and I find the executable file 3791.exe

<figure><img src=".gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

I use EventCode=1 to look for the hash of the file

<figure><img src=".gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

I then used Virustotal to look at the graph of the attacker IP address: 23.22.63.114.

<figure><img src=".gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Here, I find the SHA256 hash of the spear phishing email with custom malware attached.

9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8

<figure><img src=".gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

I then looked up the hash of the malware on virustotal.

<figure><img src=".gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

I found the hex code associated with the customized malware under the community comments.

<figure><img src=".gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

Next, I want to look for the first brute force password used. I will go back to Splunk and I will filter the src\_content and search for http\_method=POST.

<figure><img src=".gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

As seen, the password used is 12345678.

<figure><img src=".gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

To search for the password, I could have also used regex and regexr.com is a good cheat sheet source for it.

<figure><img src=".gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

Now, if I want to look for the password used in the brute force attack attempt and the src\_content looks like the following:

<figure><img src=".gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

I can use rex in my search:

<figure><img src=".gitbook/assets/image (21).png" alt=""><figcaption><p>"&#x26;passwd=(?&#x3C;password>[\w\d]+)&#x26;"</p></figcaption></figure>

In my search, it will yield:&#x20;

<figure><img src=".gitbook/assets/image (23).png" alt=""><figcaption><p>A colom with just passwords</p></figcaption></figure>

<figure><img src=".gitbook/assets/image (41).png" alt=""><figcaption><p>To answer this, I use regex again | where match(password, ".{6}") but I also knew first letter is Y</p></figcaption></figure>

<figure><img src=".gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (44).png" alt=""><figcaption><p>Found earlier when I detected the brute force attack</p></figcaption></figure>

<figure><img src=".gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

To find the average password length, I used the following search:&#x20;

<figure><img src=".gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (2).png" alt=""><figcaption><p>As seen, the average is 6</p></figcaption></figure>

<figure><img src=".gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

For this question, I will note down when the password for the brute force attack worked:

<figure><img src=".gitbook/assets/image (4).png" alt=""><figcaption><p>9:46:33.689 PM</p></figcaption></figure>

The actual login was at:

<figure><img src=".gitbook/assets/image (5).png" alt=""><figcaption><p>9:48:05.858 PM</p></figcaption></figure>

<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption><p>By subtracting the two, we get 92.17 seconds</p></figcaption></figure>

<figure><img src=".gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (47).png" alt=""><figcaption><p>There are 412 events here therefore 421 unique password were attempted</p></figcaption></figure>
