import pandas as pd
data = pd.read_csv('./training_data.txt', names=['game', 'watch', 'wtoFood', 'feed'], sep='     ')
denominator1 = float(data.shape[0])


pGame = data['game'].sum() / denominator1
pWtoFood = data['wtoFood'].sum() / denominator1
print('The probability of P(baseball_game_on_TV) is {}'.format(pGame))
print('The probability of P(out_of_cat_food) is {}'.format(pWtoFood))

denominator2 = float(data[(data['game']>0)].shape[0])
pWatchTrue = data[(data['game']>0)]['watch'].sum() / denominator2
print(pWatchTrue)
print(pWatchTrue*pGame)

denominator3 = float(data[(data['wtoFood']>0)].shape[0])
denominator3 = float(data[(data['feed']>0)].shape[0])
