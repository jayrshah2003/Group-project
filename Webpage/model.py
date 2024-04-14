
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

df = pd.read_csv('cleandata1.csv')


x = df.drop('TempHighF',axis='columns')
x = x.drop('TempLowF',axis='columns')
x = x.drop('DewPointHighF',axis='columns')
x = x.drop('DewPointLowF',axis='columns')
x = x.drop('HumidityHighPercent',axis='columns')
x = x.drop('HumidityLowPercent',axis='columns')
x = x.drop('SeaLevelPressureAvgInches',axis='columns')
x = x.drop('SeaLevelPressureLowInches',axis='columns')
x = x.drop('VisibilityHighMiles',axis='columns')
x = x.drop('VisibilityAvgMiles',axis='columns')
x = x.drop('VisibilityLowMiles',axis='columns')
x = x.drop('WindHighMPH',axis='columns')
x = x.drop('WindAvgMPH',axis='columns')
x = x.drop('WindGustMPH',axis='columns')
y = df['TempHighF']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

classify= RandomForestClassifier(n_estimators= 10, criterion="entropy")
classify.fit(x_train, y_train)

pickle.dump(classify, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1,1,1,0,0,0]]))
