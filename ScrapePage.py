from urllib.request import Request, urlopen
import bs4 as bs

url = 'https://readcomicsonline.ru/comic-list'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) '
            + 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

req = Request(url, headers=headers)
web_byte = urlopen(req).read()

webPage = web_byte.decode('utf-8')
soup = bs.BeautifulSoup(web_byte, 'lxml')

myDivs = soup.findAll("div", {"class": "media-body"})

#myDivs = soup.find("h5", {"class": "media-heading"})
#myDivs = soup.findAll("h5")#, {"class": "media-heading"})

comicNameList = []
for tag in myDivs:
    myHeader = soup.findAll("h5", {"class": "media-heading"})

    for tag in myHeader:
        comicNameList.append(tag.text)
        #print(tag.text)

comicNameList = list(set(comicNameList))
print(comicNameList)

#print(myDivs.text)
