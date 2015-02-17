from bs4 import BeautifulSoup

soup = BeautifulSoup(open("1.html"))

speaker = soup.find_all("strong")

for name in speaker:
    print name

date = soup.find_all("h4") 

for d in date:
    print d
