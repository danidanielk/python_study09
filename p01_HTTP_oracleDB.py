#기상청에서 날씨 파싱해서 DB에 저장하기.

# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4113158000
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect



con=connect("danieldb/1@192.168.123.102:1521/xe")
cur=con.cursor()



hc= HTTPConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4113158000")
resBody=hc.getresponse().read()
# print(resBody.decode())
weather=fromstring(resBody).iter("data")



for i in weather:
    sql="insert into weather values(weather_seq.nextval,'%s','%s')"%(i.find("hour").text,i.find("temp").text)
    cur.execute(sql)
con.commit()
con.close()    
print("Success")
    