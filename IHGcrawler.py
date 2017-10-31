import requests
from lxml import html

_url = 'https://www.ihg.com/hotels/cn/zh/reservation'



_headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'www.ihg.com',
'Referer':'https://www.ihg.com/hotels/cn/zh/reservation',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}


rateListUrl= "https://www.ihg.com/hotels/cn/zh/reservation/searchresult?qLng=0&qCpid=243132&qGRM=0&qBrs=ic.ki.vn.in.cp.hi.ex.rs.cv.sb.cw.ul.6c.rc.tc.sp.nd.ct&qRpn=1&srb_u=1&qCoMy=102017&qCoD=02&qRms=1&qAAR=6CBARC&qRef=df&qCiD=01&qLat=0&qCiMy=102017&qSHp=1&qWch=0&qRtP=6CBARC&qAdlt=1&qDest=SHANGHAI%252CChina%252CPeople%2527s%2BRepublic%2Bof&qRmP=3&qSrt=sDD&qSmP=3&qPSt=0&qRpp=20&qChld=0&qRRSrt=rt"
s = requests.session()
r = s.get(rateListUrl, headers= _headers)

body = html.fromstring(r.text)

#print (r.text)


sub = body.xpath('//div[contains(@id,"results_row_")]/div/div/div[2]/div[2]/div/span[2]/span[3]  | //div[contains(@id,"results_row_")]/div/div/div[2]/div[2]/div/div/div[1]/span')
name = body.xpath('//div[contains(@id,"results_row_")]/div/div/div[1]/div[1]/div[2]/div/a')
for i  in range(len(sub)):
    print(name[i].text + "*****" + sub[i].text)


