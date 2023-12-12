---
description: VirusTotal OSINT
---

# Remote Working XLS Detector

This challenge on letsdefend.io requires I visit this webpage to download a malicious file.

After downloading it, I use OSINT like VirusTotal to check it.

First question:

<figure><img src=".gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

On VirusTotal, I go to Details tab and scroll down to history to find the date created.

<figure><img src=".gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

To answer this, I go to the Detection tab and look for Bitdefender Antivirus

<figure><img src=".gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

Next question:

<figure><img src=".gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

To answer this, I head over to the relations tab and look at the  dropped files

<figure><img src=".gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

Although it says 5 dropped files, only 3 were dropped on the disk (in red marked as detections).

<figure><img src=".gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

To answer this question, I will click on the highlighted dropped file

<figure><img src=".gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

After clicking on the file, I go to details to look for the SHA-256 hash of the file.

<figure><img src=".gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

Last question of this lab is:&#x20;

<figure><img src=".gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

To answer this question, I go back to the original malicious file and go to the relations tab and I look at contacted URLs.

<figure><img src=".gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src=".gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
