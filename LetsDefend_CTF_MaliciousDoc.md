---
description: VirusTotal OSINT
---

# Malicious Doc

This lab focuses on analyzing a malicious .doc file.

I will use VirusTotal to analyze it.

First question:

<figure><img src=".gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

Next questions answer can be found with the same security vendor analysis from ClamAV:

<figure><img src=".gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

We can also see it in the behavior tab under the network communication of HTTP requests:

<figure><img src=".gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

Next question:

<figure><img src=".gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

Port 80 TCP is used to communicate here with that IP address.

The last question is: ![](<.gitbook/assets/image (50).png>)

To find the answer to this, I go to the relations tab and look for dropped files.

<figure><img src=".gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

I will click on the one with 55/72 detections.

<figure><img src=".gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

I go to the details tab and I can see the name there:

<figure><img src=".gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>
