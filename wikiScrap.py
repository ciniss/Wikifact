from bs4 import BeautifulSoup
import requests as rq

#GetTheURL

def GetFact(level_of_detail=1):
	www_link_pl='https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona'
	www_link_en='https://en.wikipedia.org/wiki/Special:Random'
	response = rq.get(www_link_en,timeout = 5)
	content = BeautifulSoup(response.content,"html.parser")
	tresc=content.find(class_='mw-parser-output')
	for i in range(level_of_detail):
	    tresc=tresc.find_next('p')
	    print(tresc.get_text())
GetFact()
