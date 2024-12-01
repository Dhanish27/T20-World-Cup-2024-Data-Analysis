from bs4 import BeautifulSoup
import requests
html_text=requests.get("https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2024-15946").text
soup=BeautifulSoup(html_text,'lxml')
file = open('Table1.csv','w')

table=soup.find('table')            #Extracting Table html code from main code

data=table.find_all('tr')           #Extracting All rows html code from the table

for d in data:                      #Extracting data  row by row
    rows=d.find_all('td')
    row=""                         #Creating empty string so that the row data is concatenated and passed as an single input to the txt
    
    for td in range (0,len(rows)-1):        #Extracting and concataned all individual element of the rows

        if(td==0):                          #To avoid first row first value getting , in front
            row=str(rows[td].text)
        else:
            row=row+","+str(rows[td].text)

    file.write(row+"\n")                    #inputed to txt