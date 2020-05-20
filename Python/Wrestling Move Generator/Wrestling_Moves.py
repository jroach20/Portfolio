from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from random import randrange
  

""" All information is scraped from Wikipedia.
You must have the file "wrestling Weblist.txt in the same 
directory as this file for the program to work.
Run MoveGenerator first before running Reader."""

def scraper(tag):
    double_quote = '"'
    
    par_split =re.split(r'[.!?]+',tag)
    par_split.insert(len(par_split),double_quote)
            
    
    if(tag == 'p'):
        if len(par_split) <2 or 3 or 4:
                text = (" ".join(map(str,tag)))
                text = (' '.join(text.split()))
    
    else:
        text = (" ".join(map(str,par_split)))
        text = (' '.join(text.split()))
    
    return text

# read urls of websites from text file
def MoveGenerator():
    file = open("Fact Lists\wrestling.txt","w+",encoding = "utf-8")
    list_open = open("Web Lists\wrestling WebList.txt","r")
    read_list = list_open.read()
    url = read_list.split("\n")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    
    
    for x in range (4):
        req = Request (''+url[x]+'',headers = headers)
        sauce = urlopen(req).read()
        soup = BeautifulSoup(sauce, 'lxml')
        for header in soup.find_all('h4') or soup.find_all("h5") or soup.find_all("h6") or soup.find_all("h3"):
        
            
            span = header.find_next('span')
            head = span.text
            move = scraper(head)
                        
            for a in soup.findAll('a'):
                a.replaceWithChildren()
            
            for i in soup.findAll('i'):
                i.replaceWithChildren()
                
            for sup in soup.findAll('sup'):
                sup.decompose()
            
            p = header.find_next("p")
            
            text = scraper(p.text)
            
            
            
            
            file.write("[ \""+move+": "+"\""+text+"],\n")

def reader():
    data = []
    with open('Fact Lists\wrestling.txt', 'r') as f:
        data = f.readlines()
    
    print(data[randrange(len(data))])


# Run first if you haven't already: MoveGenerator()
reader()