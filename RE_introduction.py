import re
text = open("re.txt")
for line in text:
    line = line.rstrip()
    if re.search('ovo je bitno', line): #ako postoji ovaj string ,vraca True
        print(line)
    if re.search('^ovo je bitno', line): #ako pocinje
        print(line)
    print( re.findall('[gG]', line))#vraca listu,praznu ili sa nekoliko elemenata


