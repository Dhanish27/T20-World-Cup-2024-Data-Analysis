from bs4 import BeautifulSoup
import requests
import pandas as pd

#Batters

html_text=requests.get("https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946").text
soup=BeautifulSoup(html_text,'lxml')
table=soup.find('table',class_="ds-w-full ds-table ds-table-xs ds-table-auto ds-w-full ds-overflow-scroll ds-scrollbar-hide")
data=table.find_all('tr')
file = open('PlayerDescription.csv','w',encoding='utf-8')
for d in data:
    td_elements = d.find_all('td')
    player=td_elements[0]
    a_tag = player.find('a')
    if a_tag and 'href' in a_tag.attrs:
        internal_html_text=requests.get("https://www.espncricinfo.com"+str(a_tag['href'])).text
        soup1=BeautifulSoup(internal_html_text,'lxml')
        container = soup1.find('div',class_="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8")
        text=""
        text = ""
        for i in range(6):  # Iterate from 0 to 5
            try:
                text +=  container.find_all('span', class_="ds-text-title-s ds-font-bold ds-text-typo")[i].text+", "
            except IndexError:
                # Handle the case where the index is out of range
                text += ", "  # Add an empty string or some placeholder if needed
            if(i==5):
                photo_box = soup1.find('div', class_="ds-w-full ds-bg-fill-content-prime ds-overflow-hidden ds-rounded-xl ds-border ds-border-line")
                text += "("+photo_box.find('img')['src']+")"+", "
                text += soup1.find('div',class_="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-y-4").find('span',class_="ds-cursor-pointer ds-inline-flex ds-items-start ds-leading-none").text
        print(text)
        file.write(text + "\n")

#Bowlers
html_text=requests.get("https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2024-15946").text
soup=BeautifulSoup(html_text,'lxml')
table=soup.find('table',class_="ds-w-full ds-table ds-table-xs ds-table-auto ds-w-full ds-overflow-scroll ds-scrollbar-hide")
data=table.find_all('tr')

for d in data:
    td_elements = d.find_all('td')
    player=td_elements[0]
    a_tag = player.find('a')
    if a_tag and 'href' in a_tag.attrs:
        internal_html_text=requests.get("https://www.espncricinfo.com"+str(a_tag['href'])).text
        soup1=BeautifulSoup(internal_html_text,'lxml')
        container = soup1.find('div',class_="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8")
        text=""
        text = ""
        for i in range(6):  # Iterate from 0 to 5
            try:
                text +=  container.find_all('span', class_="ds-text-title-s ds-font-bold ds-text-typo")[i].text+", "
            except IndexError:
                # Handle the case where the index is out of range
                text += ", "  # Add an empty string or some placeholder if needed
            if(i==5):
                photo_box = soup1.find('div', class_="ds-w-full ds-bg-fill-content-prime ds-overflow-hidden ds-rounded-xl ds-border ds-border-line")
                text += "("+photo_box.find('img')['src']+")"", "
                text += soup1.find('div',class_="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-y-4").find('span',class_="ds-cursor-pointer ds-inline-flex ds-items-start ds-leading-none").text
        print(text)
        file.write(text + "\n")

file.close

            