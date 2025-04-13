import pandas as pd
import csv
from google_play_scraper import reviews, Sort

scrap, _ = reviews(
    'com.telkomsel.telkomselcm',
    lang='id',
    country='id',
    sort = Sort.MOST_RELEVANT,
    count=10000
)

with open('ulasan_mytelkomsel.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrap:
        writer.writerow([review['content']])


df = pd.DataFrame(scrap)
df.shape
df.head()
df.to_csv('ulasan_mytelkomsel.csv',index=False)
df = pd.DataFrame(scrap)
jumlah_ulasan, jumlah_kolom = df.shape
print(jumlah_ulasan,jumlah_kolom)