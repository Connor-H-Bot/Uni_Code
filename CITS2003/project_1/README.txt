These scripts were created by Connor Harris (23208009)

I had the most peculiar issue when creating the "common_words script" so this is really important.

After running it a few times, it refuses to to create the new files. 
I have no idea why this happened at all, and I was too proud (or embarrassed) to post it on stack overflow so if this error happens you'll need to reboot your linux distro and run the script again. It can happen the first time you run it, or it could happen on the hundredth time. Because I struggled to replicate this bug, I could not fix it within a reasonable amount of time. 

If the program abruptly ends and the temp files aren't deleted, it SHOULD still work fine as the initial writes in each file have been set to overwrite anything already held in them file. 

"Malaria_incidence" is compatible with "MACOSX" and the "5.10.76-linuxkit", but "common_words" will not work on MACOSX due to the extensive use of commands that have slight differences (ie SED and AWK). 

Apart from that, the scripts have been made to scale with larger data sets (within reason). 





