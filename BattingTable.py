from bs4 import BeautifulSoup
import requests
import pandas as pd
html_text=requests.get("https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946").text
soup=BeautifulSoup(html_text,'lxml')
file = open('BattingTable.txt','w')
table = soup.find('table', class_="ds-w-full ds-table ds-table-xs ds-table-auto ds-w-full ds-overflow-scroll ds-scrollbar-hide")

if table:
    # Extract data as before
    data = []
    headers = []

    # Extract headers
    for td in table.find('tr'):
        headers.append(td.text.strip())

    # Extract rows
    for tr in table.find_all('tr')[1:]:  # Skip the header row
        row = []
        for td in tr.find_all('td'):
            row.append(td.text.strip())
        data.append(row)

    # Convert to DataFrame for better visualization and manipulation
    df = pd.DataFrame(data,columns=headers)
    df.to_csv('BattingTable.csv', index=False)
else:
    print("Table not found")