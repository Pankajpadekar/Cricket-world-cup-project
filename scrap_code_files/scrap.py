from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

url = "https://www.espncricinfo.com/records/tournament/team-match-results/icc-cricket-world-cup-2023-24-15338"

parse = requests.get(url)
htmlContent = parse.content
# print(htmlContent)

soup =  BeautifulSoup(htmlContent, 'html.parser')

table = soup.find('table')

table_data  = []
headers = []

for i, row in enumerate(table.find_all('tr')):
    columns = row.find_all(['td', 'thead'])
    row_data = [column.text.strip() for column in columns]
    # print(row_data)


    if i == 0:
        headers = row_data
    else:
        row_dict = dict(zip(headers, row_data))
        table_data.append(row_dict)

    match_summary = json.dumps(table_data, indent=2)

    with open('match_summary.json', 'w') as file:
        file.write(match_summary)

    df = pd.DataFrame(table_data, columns=headers)

    print(df)