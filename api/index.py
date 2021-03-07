#coding:utf-8
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from lxml import etree
import re
app = FastAPI()

origins = [
	"http://127.0.0.1:8000",
	"http://localhost",
	"http://localhost:8000",
	"*",
	]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=['*'],
	)
@app.get("/")
async def read_root():
	return {"剧集":"没有剧集"}

@app.get("/iqiyi/{name}")
async def read_item(name: str):
	url = "https://so.iqiyi.com/so/q_" + str(name)
	payload={}
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

	response = requests.request("GET", url, headers=headers, data=payload)
	content = response.content
	html = etree.HTML(content)
	data = html.xpath('//*[@id="__layout"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul[2]/li/a')
	result = []
	for i in data:
	  if 'iqiyi' in i.attrib.get('href'):
	    # print(i.attrib.get('href'))
	    # print(i.attrib.get('title'))
	    name  = i.attrib.get('title')
	    key = re.findall(r"\d+", name)[0]
	    value = "https:"+ i.attrib.get('href')
	    #result[key] = value
	    result.append({"id":key,"src":value})
	return result

