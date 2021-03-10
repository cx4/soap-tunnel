
#coding:utf-8
from requests_html import HTMLSession
session = HTMLSession()
url = "https://so.iqiyi.com/so/q_%E8%B5%98%E5%A9%BF"

headers = {
  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'same-site',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document'
}

response = session.get(url,headers=headers)
#response = requests.request("GET", url, headers=headers, data=payload)

content = response.html

# soup = BeautifulSoup(content,'lxml')
# album_list = soup.find_all('li',_class='album-list')
# print(album_list) 
# html = etree.HTML(content)
data = content.xpath('//*[@id="__layout"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul[1]/li/a')

for i in data:
  if 'iqiyi' in i.attrs['href']:
    print(i.attrs['title'])
    print(i.attrs['href'])
  #   order = i.attrib.get('title')
  #   o = re.findall(r"\d+", order)
  #   print(o)
  #   print(i.attrib.get('href'))
# print(data)