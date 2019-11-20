import pandas as pd
data = pd.read_csv('./training_data.txt', names=['game', 'watch', 'wtoFood', 'feed'], sep='     ')

denom1 = float(data.shape[0])
pGame = data['game'].sum() / denom1
pWtoFood = data['wtoFood'].sum() / denom1
print(data['game'].sum(), denom1) # 111, 365
print('The probability of P(baseball_game_on_TV) is {}'.format(pGame)) # 0.30410
print(data['wtoFood'].sum(), denom1) # 62, 365
print('The probability of P(out_of_cat_food) is {}'.format(pWtoFood)) # 0.16986

denom2t = float(data[(data['game']==1)].shape[0]) # 111
denom2f = float(data[(data['game']==0)].shape[0]) # 254
watch = data[(data['game']>0)&(data['watch']>0)].sum()['watch'] # 103
pWatchTrue = watch / denom2t # 103/111
pWatchFalse = watch / denom2f # 103/254
print('The probability of P(Geogrge_watches_TV|basket_game_on_TV) is {}'.format(pWatchTrue))
print('The probability of P(Geogrge_watches_TV|not(basket_game_on_TV)) is {}'.format(pWatchFalse))

denom3tt = float(data[(data['wtoFood']==1)&(data['watch']==1)].shape[0]) # 24
denom3tf = float(data[(data['wtoFood']==1)&(data['watch']==0)].shape[0]) # 38
denom3ft = float(data[(data['wtoFood']==0)&(data['watch']==1)].shape[0]) # 109
denom3ff = float(data[(data['wtoFood']==0)&(data['watch']==0)].shape[0]) # 194
feedTT = data[(data['wtoFood']==1)&(data['watch']==1)&(data['feed']==1)].sum()['feed'] # 1
feedTF = data[(data['wtoFood']==1)&(data['watch']==0)&(data['feed']==1)].sum()['feed'] # 12
feedFT = data[(data['wtoFood']==0)&(data['watch']==1)&(data['feed']==1)].sum()['feed'] # 77
feedFF = data[(data['wtoFood']==0)&(data['watch']==0)&(data['feed']==1)].sum()['feed'] # 186
pFeedTT = feedTT / denom3tt
pFeedTF = feedTF / denom3tf
pFeedFT = feedFT / denom3ft
pFeedFF = feedFF / denom3ff
print('The probability of P(Geogrge_feeds_cat|out_of_cat_food, Geogrge_watches_TV) is {}'.format(pFeedTT))
print('The probability of P(Geogrge_feeds_cat|out_of_cat_food, not(Geogrge_watches_TV)) is {}'.format(pFeedTF))
print('The probability of P(Geogrge_feeds_cat|not(out_of_cat_food), Geogrge_watches_TV) is {}'.format(pFeedFT))
print('The probability of P(Geogrge_feeds_cat|not(out_of_cat_food), not(Geogrge_watches_TV)) is {}'.format(pFeedFF))

# For Task5
d11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)].shape[0]
n11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)&(data['feed']==0)].shape[0]

d11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)].shape[0]
n11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)&(data['feed']==0)].shape[0]

d11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)].shape[0]
n11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)&(data['feed']==0)].shape[0]

d11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)].shape[0]
n11 = data[(data['game']==1)&(data['watch']==1)&(data['wtoFood']==1)&(data['feed']==0)].shape[0]

# Task 5
N = data[(data['game']==1)&(data['feed']==0)].shape[0] / denom1
D = pGame
print('ttt', N, D, data[(data['game']==1)&(data['feed']==0)].shape[0])
print("The probability of P(not(George Feeds cat)|Baseball Game on TV) is {}".format(N/D))
