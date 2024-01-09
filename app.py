# Retrieving Links and Text In Bs4 - Web Scraping
# Using Python + BeautifulSoup

import bs4
import requests



url = "https://pypi.org/project/beautifulsoup4/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text ,'html.parser')
#  print(soup.prettify())

# for para in soup.find_all('p'):
#     print(para.text)


# for links in soup.find('a'):
#     link = links.get('href')
#     if link[0:3] == "pip" and link != "#":
#         print("https://pypi.org" + links[1:len(link)])
#     elif link[0] == "/" and link != "#":
#         print("https://pypi.org" + links)
#     elif link != "#":
#         print(link)

url2 = "https://www.youtube.com/results?search_query=hindi+coding+harry+code+with+python+"
data = requests.get(url2)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
for link in soup.find_all('a'):
    link = link.get("href")
    if link[0:3] == "/s":
        print("https://www.youtube.com/" + link)







