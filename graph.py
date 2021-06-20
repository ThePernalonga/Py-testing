# Just testing XML parsing

import xml.dom.minidom

doc = xml.dom.minidom.parse("test.xml")

nos = doc.getElementsByTagName("node")

for numero in nos:
  print(numero.getAttribute("id"))