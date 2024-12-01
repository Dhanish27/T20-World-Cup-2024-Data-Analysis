import csv
import requests
from bs4 import BeautifulSoup

# Get the HTML content
html_text = requests.get("https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/west-indies-vs-papua-new-guinea-2nd-match-group-c-1415702/full-scorecard").text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')
file = open('BattingSummary.txt','w')
# Find the table in the HTML content
table = soup.find_all('table',class_="ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table")
print(len(table))
# for tr in table.find_all('tr')[1::2]:
#     row=""
#     a=10
#     for td in tr.find_all('td'):
#         text=td.text
#         row=row+text+","
#         if(text=="TOTAL" or text=="Extras"):
#             a=100
#     if(a==100):
#         break
#     row=row[:-1]
#     row=row.replace("†","")
#     print(row)
#     file.write(row + "\n")
# file.close()

# # Check if the table is found
# # if table:
# #     # Open a file to write the data with utf-8 encoding to handle special characters
# #     with open('BattingSummary.csv', 'w', newline='', encoding='utf-8') as file:
# #         writer = csv.writer(file)
        
# #         # Extract all rows in the table
# #         rows = table.find_all('tr')
        
# #         # Iterate over each row
# #         for row in rows:
# #             # Extract all columns in the row
# #             cols = row.find_all('td')
            
# #             # Initialize a list to store column texts
# #             col_texts = []
# #             for col in cols:
# #                 text = col.text.strip()
# #                 if text.lower() == "extras":
# #                     break
# #                 col_texts.append(text)
            
# #             # Write the row data to the CSV file if the row has data
# #             if col_texts:
# #                 writer.writerow(col_texts)
# # else:
# #     print("Table not found.")


# ds-w-full ds-table ds-table-md ds-table-auto  ci-scorecard-table
# ds-w-full ds-table ds-table-md ds-table-auto  ci-scorecard-table