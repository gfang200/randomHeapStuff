import bs4
from xml.dom import minidom
import urllib2
import re
import json

start = urllib2.build_opener()
start.addheaders = [('User-Agent', 'Mozilla/5.0')]
heap = start.open('https://heapanalytics.com/about')

read_heaps = heap.read()

start.close()



soup = bs4.BeautifulSoup(read_heaps, 'html.parser')

li = soup.findAll('li', {"class": re.compile("team-.*")})

dict_out = {}

for each in li:


    name = each.h1.text
    name_out = name.strip().split('\n')[0].strip()
 
    # print name_out.split(' ')
    first, last = name_out.split(' ')[0],name_out.split(' ')[-1] 

    site = each.div

    # print each
    site_out = site.get('style')
    image = site_out.split('(')[1].split(')')[0]

    # print first
    # print last
    # print image
    # print "-"

    dict_out[name_out] = {'first_name': first, 'last_name': last, 'image_url': image}

# print dict_out

jsono = json.dumps(dict_out)

fileout = open('data.json',"w")
fileout.write(jsono)
fileout.close()