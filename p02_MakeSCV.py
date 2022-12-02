from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=411315800

hc=HTTPConnection("www.kma.go.kr")
hc.request("GET","/wid/queryDFSRSS.jsp?zone=411315800")
resbody=hc.getresponse().read()
# print(resbody.decode())
weather=fromstring(resbody).iter("data")

file=open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test3.csv","w",encoding="UTF-8")

for i in weather:
    file.write(i.find("hour").text)
    file.write("")
    file.write(i.find("temp").text)
    file.write("----------------")

file.close()






