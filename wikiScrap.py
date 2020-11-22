from bs4 import BeautifulSoup
import requests as rq

#GetTheURL

def GetFact(level_of_detail=1,language="en"):

	language_options={"pl":"https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona",
						"en":"https://en.wikipedia.org/wiki/Special:Random"}
	response = rq.get(language_options[language],timeout = 5)
	content = BeautifulSoup(response.content,"html.parser")
	tresc=content.find(class_='mw-parser-output')
	for i in range(level_of_detail):
	    tresc=tresc.find_next('p')
	    print(tresc.get_text())
GetFact()
