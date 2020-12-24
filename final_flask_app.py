from app import db, NFLRankingTable
from bs4 import BeautifulSoup
import requests
url = 'https://www.teamrankings.com/nfl/'
r = requests.get(url)
soup = BeautifulSoup(r.text)
table = soup.find('table')
rows = table.findAll('tr')
clean_data = []
for row in rows[1:]:
    link = row.find('a')["href"]
    stripped_list = list(row.stripped_strings)
    stripped_list.append(link)
    clean_data.append(stripped_list)
print(clean_data)
def main():
    db.drop_all()
    db.create_all()
    for row in clean_data:
        new_row = NFLRankingTable(rank = row[0], rating = row[1], team = row[2], proj_win = row [3], proj_loss = row[4], play_off = row[5], sb_win = row[6])
        db.session.add(new_row)
        db.session.commit()
if __name__ == "__main__":
    main()