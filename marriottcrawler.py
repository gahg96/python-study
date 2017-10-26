# -*- coding:utf-8 -*-   
#获取并打印marrioot首页的html  

import requests
from lxml import html

_url = 'http://www.marriott.com.cn/search/findHotels.mi'

_headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'www.marriott.com.cn',
'Referer':'http://www.marriott.com.cn/default.mi',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

resp = requests.get(_url, headers= _headers)
cookies = resp.cookies

cityname = input("what is city name? Beijing :1 ,Shanghai :2, Guangzhou :3,Shenzhen :4****")
if (cityname == "1"):
    city = "Beijing"
elif (cityname=="2"):
    city = "Shanghai"
elif (cityname=="3"):
    city = "Guangzhou"
elif (cityname=="4"):
    city = "Shenzhen"
else:
    city = "Shanghai"

starttime = input("please input start time, example:2017-10-27***")

endtime = input("please input end time, example:2017-10-29***")



#url ="http://www.marriott.com.cn/search/submitSearch.mi?searchType=InCity&groupCode=&searchRadius=&poiName=&poiCity=%E5%8C%97%E4%BA%AC&recordsPerPage=20&for-hotels-nearme=%E9%9D%A0%E8%BF%91&destinationAddress.destination=%E5%8C%97%E4%BA%AC%2C+China&singleSearch=true&singleSearchAutoSuggest=false&autoSuggestItemType=Unmatched&clickToSearch=false&destinationAddress.latitude=39.906011&destinationAddress.longitude=116.387911&destinationAddress.cityPopulation=0.0&destinationAddress.cityPopulationDensity=0.0&destinationAddress.city=%E5%8C%97%E4%BA%AC&destinationAddress.stateProvince=&destinationAddress.country=CN&airportCode=&fromToDate=7+%E6%9C%88+28%E6%97%A5%2C+%E5%91%A8%E5%9B%9B&fromToDate_submit=2016-07-28&fromDate=2016-07-28&toDate=2016-07-29&lengthOfStay=1&roomCountBox=1&roomCount=1&guestCountBox=1&guestCount=1&clusterCode=none&corporateCode="

#url ="http://www.marriott.com.cn/search/submitSearch.mi?searchType=InCity&groupCode=&searchRadius=&poiName=&poiCity=&recordsPerPage=20&for-hotels-nearme=%E9%9D%A0%E8%BF%91&destinationAddress.destination=Shanghai%2C+China&singleSearch=true&singleSearchAutoSuggest=true&autoSuggestItemType=Unmatched&clickToSearch=false&destinationAddress.latitude=31.232225&destinationAddress.longitude=121.469197&destinationAddress.cityPopulation=0.0&destinationAddress.cityPopulationDensity=0.0&destinationAddress.city=Shanghai&destinationAddress.stateProvince=&destinationAddress.country=CN&airportCode=&fromToDate=10+%E6%9C%88+27%E6%97%A5%2C+%E5%91%A8%E4%BA%94&fromToDate_submit=2017-10-27&fromDate=2017-10-27&toDate=2017-10-29&lengthOfStay=2&roomCountBox=1&roomCount=1&guestCountBox=1&guestCount=1&clusterCode=other&corporateCode=IBM"
url ="http://www.marriott.com.cn/search/submitSearch.mi?searchType=InCity&groupCode=&searchRadius=&poiName=&poiCity=&recordsPerPage=20&for-hotels-nearme=%E9%9D%A0%E8%BF%91&destinationAddress.destination="+ city + "%2C+China&singleSearch=true&singleSearchAutoSuggest=true&autoSuggestItemType=Unmatched&clickToSearch=false&destinationAddress.latitude=&destinationAddress.longitude=&destinationAddress.cityPopulation=0.0&destinationAddress.cityPopulationDensity=0.0&destinationAddress.city=" + city+ "&destinationAddress.stateProvince=&destinationAddress.country=CN&airportCode=&fromToDate=10+%E6%9C%88+27%E6%97%A5%2C+%E5%91%A8%E4%BA%94&fromToDate_submit=2017-10-27&fromDate="+starttime+ "&toDate="+ endtime+"&lengthOfStay=2&roomCountBox=1&roomCount=1&guestCountBox=1&guestCount=1&clusterCode=other&corporateCode=IBM"
r = requests.get(url, headers = _headers,  cookies = cookies)
body = html.fromstring(r.text)
sub = body.xpath('//span[@class="t-price"]')
name = body.xpath('//span[@class="l-display-none"]')
for i  in range(len(name)):
    print(name[i].text +  sub[i].text)

