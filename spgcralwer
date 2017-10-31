
import requests
from lxml import html

_url = 'https://www.starwoodhotels.com/preferredguest/account/sign_in.html?language=zh_CN'



_headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'www.starwoodhotels.com',
'Referer':'https://www.starwoodhotels.com/corporate/index.html',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}


rateListUrl= "https://www.starwoodhotels.com/preferredguest/search/results/detail.html?skinCode=SPG&localeCode=zh_CN&iATANumber=&country=CN&stateProvince=SHA&romanStateProvince=&chinaStateProvince=SHA&japanStateProvince=&city=Shanghai&arrivalDate=17%E5%B9%B410%E6%9C%8831%E6%97%A5&departureDate=17%E5%B9%B411%E6%9C%8801%E6%97%A5&rp=corporateAccountNumber%253A18000&numberOfRooms=1&numberOfAdults=1&numberOfChildren=0"
s = requests.session()
r = s.post(rateListUrl, headers= _headers)
#print (str(r.status_code ))
#print (r.request.headers)
#print (r.text)

body = html.fromstring(r.text)
sub = body.xpath('//span[@class="currency"]')

name = body.xpath('//*[@id="searchEssentials"]/div[1]/h2/a[1]/text()')
print (range(len(sub)))
print (range(len(name)))

for i  in range(len(sub)):
    print(name[i] + sub[i].text)


