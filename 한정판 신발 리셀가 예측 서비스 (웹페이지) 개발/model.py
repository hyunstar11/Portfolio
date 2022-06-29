import random 
random.seed(1)
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, make_scorer
# from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso

dff = pd.read_csv('StockX3.csv')
dff['Order Date'] = pd.to_datetime(dff['Order Date'])
dff['Release Date'] = pd.to_datetime(dff['Release Date'])
condition = ((dff['Order Date'] > '2018-11-30') & (dff['Order Date'] < '2019-01-01'))
dff = dff[condition]

df2 = dff
df2 = df2.drop(columns='Order Date')
df2 = df2.drop(columns='Release Date')

from sklearn.model_selection import train_test_split 
train, test = train_test_split(df2, train_size = 0.80, shuffle=True, random_state=121)

target = 'Sale Price'
features = df2.drop(columns=[target]).columns
X_train = train[features]
Y_train = train[target]
X_test = test[features]
Y_test = test[target]

# Train lasso model
lasso = Lasso(alpha=1e-1)
final_model = lasso.fit(X_train, Y_train)
Y_pred = final_model.predict(X_test)
#print('R²: %.2f' % r2_score(Y_test, Y_pred))

import pickle 
with open('lasso0.pkl','wb') as pickle_file:
    pickle.dump(final_model, pickle_file)

final_model.save('test.h5')



