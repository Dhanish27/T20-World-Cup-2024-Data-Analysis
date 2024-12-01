from bs4 import BeautifulSoup
import requests
import pandas as pd
html_text=requests.get("https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2024-15946").text
soup=BeautifulSoup(html_text,'lxml')
table=soup.find('table',class_="ds-w-full ds-table ds-table-xs ds-table-auto ds-w-full ds-overflow-scroll ds-scrollbar-hide")
data=table.find_all('tr')
file = open('BattingSummary.csv','w',encoding='utf-8')

for d in data:
        # Ensure that there are enough columns in the row
        td_elements = d.find_all('td')
        if len(td_elements) > 6:
            Id = td_elements[6]
            a_tag = Id.find('a')
            # Ensure that a_tag is found
            if a_tag and 'href' in a_tag.attrs:
                internal_html_text=requests.get("https://www.espncricinfo.com"+str(a_tag['href'])).text
                print("https://www.espncricinfo.com"+str(a_tag['href']))
                soup1=BeautifulSoup(internal_html_text,'lxml')
                table1=soup1.find('table')
                i=1
                tables = soup1.find_all('table',class_="ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table")
                if(len(tables)>1):
                    match=soup1.find('div',class_="ds-flex ds-px-4 ds-border-b ds-border-line ds-py-3 ds-bg-ui-fill-translucent-hover").find('span',class_="ds-text-title-xs ds-font-bold ds-capitalize").text + " vs " + soup1.find_all('div',class_="ds-flex ds-px-4 ds-border-b ds-border-line ds-py-3 ds-bg-ui-fill-translucent-hover")[1].find('span',class_="ds-text-title-xs ds-font-bold ds-capitalize").text
                    print(match)
                    for tr in table1.find_all('tr')[0:]:
                        row=""
                        a=10
                        for td in tr.find_all('td'):
                            text=td.text
                            row=row+text+","
                            if(text=="TOTAL"or text =="Extras" ):
                                a=100
                            
                        if(a==100):
                            a=10
                            break
                        if(len(row)>5):
                            row=row+str(i)
                            row=row+","+match
                            teaminnings=soup1.find('div',class_="ds-flex ds-px-4 ds-border-b ds-border-line ds-py-3 ds-bg-ui-fill-translucent-hover").find('span',class_="ds-text-title-xs ds-font-bold ds-capitalize").text
                            row=row+","+teaminnings
                            i=i+1
                        # row=row[:-1]
                        
                        row=row.replace("†","")
                        row=row.replace(",,",",")
                        print(row)
                        if(len(row)>5):
                            file.write(row + "\n")

                    
                    
                
                    table2=tables[1]
                    i=1
                    for tr in table2.find_all('tr')[0:]:
                        row=""
                        a=10
                        for td in tr.find_all('td'):
                            text=td.text
                            row=row+text+","
                            if(text=="TOTAL"or text =="Extras"):
                                a=100
                            
                        if(a==100):
                            a=10
                            break
                        if(len(row)>5):
                            row=row+str(i)
                            row=row+","+match
                            teaminnings=soup1.find_all('div',class_="ds-flex ds-px-4 ds-border-b ds-border-line ds-py-3 ds-bg-ui-fill-translucent-hover")[1].find('span',class_="ds-text-title-xs ds-font-bold ds-capitalize").text
                            row=row+","+teaminnings
                            i=i+1
                        # row=row[:-1]
                        
                        row=row.replace("†","")
                        row=row.replace(",,",",")
                        print(row)
                        if(len(row)>5):
                            file.write(row + "\n")
                
file.close()