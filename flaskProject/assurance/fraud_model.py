import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier


data = pd.read_csv('modelefraud.csv')
data = data.drop(['Unnamed: 0', 'coefBonusMalus'], axis=1)
data = data[data['Fraud'] != 8]
y= data['Fraud']
X= data.drop(['Fraud'], axis=1)

print(X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
model = CatBoostClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open('fraudmodel.pkl', 'wb'))

