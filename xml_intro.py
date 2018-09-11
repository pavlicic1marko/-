import xml.etree.ElementTree as ET
e = ET.parse('Library.xml').getroot()
print(e) #object location in memory
lst=e.findall("dict//dict") #tags in the html file "<dict> is the parent tag of <key>"
print(len(lst))
print(list)
for ii in lst:
    print(ii.find('key').text)
