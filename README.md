This is a simple QR Code generator program using the qrcode and pillow(PIL)
libraries to generate a qr code based on the link provided.

This program was created to get around the expirations dates and signups
that different onlines websites offer when generating QR code.

I got the idea to research the creation of a program like this more deeply
after seeing a colleague use a script preinstalled on their macbook. He
indicated that websites that offer the QR Code service expire the QR code
after a set amount of time whilst also using the QR code they generate to
pull traffic to their websites.

After a quick overview of some of what went into QR code generation, I 
simply asked google for a script to create qr code from links, copied and
walked through the code it outlined.

The most difficult part to this was figuring out that the missing 
dependancy PIL is installed via pip install pillow. Its name isnt clear
from just the error readout. I was able to discover this after another
simple google search.

What does it mean for websites that offer this service when its this
simple to recreate it for oneself with just two google searches and python?
