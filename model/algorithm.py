import re as re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Weighted Filtering Function


def calculate(restoran_df, restoran_type, restoran_area, prio_1, prio_2):
    value_df = []

    type_prio = (0.8 if prio_1 == "Jenis" else 0.15 if prio_2 == "Jenis" else 0.05)
    area_prio = (0.8 if prio_1 == "Lokasi" else 0.15 if prio_2 == "Lokasi" else 0.05)
    rating_prio = (0.8 if prio_1 == "Rating" else 0.15 if prio_2 == "Rating" else 0.05)

    for x in range(len(restoran_df)):
        resto_value = 0

        if restoran_type in str(restoran_df[restoran_df['Restaurant_ID'] == x]['Type'].values[0]):
            resto_value += type_prio * 1

        if restoran_area == str(restoran_df[restoran_df['Restaurant_ID'] == x]['Area'].values[0]):
            resto_value += area_prio * 1

        resto_value += rating_prio * (restoran_df[restoran_df['Restaurant_ID'] == x]['Rating'].values[0]/5)

        value_df.append(resto_value)

    return value_df


def weighted_filtering(restoran_df, jenis, lokasi, prio_1, prio_2):
    recommendation = []

    if 'Value' in restoran_df.columns:
        restoran_df = restoran_df.drop(['Value'], axis=1)

    value_df = calculate(restoran_df, jenis, lokasi, prio_1, prio_2)
    restoran_df['Value'] = value_df
    restoran_df = restoran_df.sort_values(by='Value', ascending=False)

    for x in range(3):
        recommendation.append(restoran_df['Name'].values[x])

    return recommendation

# Content Based Filtering


def get_important_features(restoran_df):
    important_features = []
    for i in range(0, restoran_df.shape[0]):
        x = (str(restoran_df['Type'][i])+' '+str(restoran_df['Area'][i]))
        x = x.lower()
        x = re.sub(r'[^.,a-zA-Z0-9 \n\.]', ' ', x)
        x = re.sub(r'[^\w\s]', '', x)
        x = re.sub('[\s]+', ' ', x)
        important_features.append(x)

    return important_features


def content_based_filtering(restoran_df, nama):
    recommedation = []

    restoran_df['Important_Features'] = get_important_features(restoran_df)

    cm = CountVectorizer().fit_transform(restoran_df['Important_Features'])
    cs = cosine_similarity(cm)

    product_id = restoran_df[restoran_df["Name"]
                             == nama]['Restaurant_ID'].values[0]

    scores = list(enumerate(cs[product_id]))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:4]

    j = 0
    for item in sorted_scores:
        recommedation.append(
            restoran_df[restoran_df['Restaurant_ID'] == sorted_scores[j][0]]['Name'].values[0])
        j += 1

    return recommedation
