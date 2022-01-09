import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv('BMmodel.csv')


data = data.drop(columns=['Unnamed: 0'], axis=1)
y = data['classeBonusMalus']
X = data.drop(['classeBonusMalus'], axis=1)

print(X.columns)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=43)
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=0)


dt.fit(X_train, y_train)
print('Le train score est :', dt.score(X_train, y_train))
print('Le test score est :', dt.score(X_test, y_test))
pickle.dump(dt, open('modelBM.pkl', 'wb'))
