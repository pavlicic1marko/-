import urllib.request
urllib.request.urlretrieve("https://grad.ucla.edu/asis/agep/advcv.pdf","new.pdf")

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('https://viphouse.rs/products/27031/6360.jpg').read()
fhand = open('6360.jpg', 'wb')
fhand.write(img)
fhand.close()
