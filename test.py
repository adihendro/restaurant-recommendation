import pandas as pd
from model import algorithm

# Data Loading
restoran_df = pd.read_csv('./data/dataFinal.csv')

# Data Cleaning
restoran_df = restoran_df.drop(['Unnamed: 0','Price'],axis=1)
restoran_df = restoran_df.drop(index=135, axis=0)

jenis = "Bar"
lokasi = "Thamrin"

prio_1 = "lokasi"
prio_2 = "jenis"

nama = 'OKU - Hotel Indonesia Kempinski'

recommedation_1 = algorithm.weighted_filtering(restoran_df, jenis, lokasi, prio_1, prio_2)

for x in range(3):
    print(recommedation_1[x])

recommedation_2 = algorithm.content_based_filtering(restoran_df, nama)

for x in range(3):
    print(recommedation_2[x])

