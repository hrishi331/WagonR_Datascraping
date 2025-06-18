from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score, root_mean_squared_error 
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.header("WagonR Resale Price Predictor") 
df =pd.read_csv("database/WagonR_DB_Cleaned1.csv")

df =df.drop('Unnamed: 0',axis=1)

X = df.drop('Price',axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def encoder(X_train,X_test):
    '''
    Returns X_train and X_test
    '''
    cats_v = X_train['Variant'].unique()
    mapper_v = {label : ind for ind,label in enumerate(cats_v)}
    cats_l = X_train['Location'].unique()
    mapper_l = {label : ind for ind,label in enumerate(cats_l)}
    cats_f = X_train['Fuel'].unique()
    mapper_f = {label : ind for ind,label in enumerate(cats_f)}

    X_train['Variant'] = X_train['Variant'].map(mapper_v).fillna(-1).astype(int)
    X_test['Variant'] = X_test['Variant'].map(mapper_v).fillna(-1).astype(int)
    X_train['Location'] = X_train['Location'].map(mapper_l).fillna(-1).astype(int)
    X_test['Location'] = X_test['Location'].map(mapper_l).fillna(-1).astype(int)
    X_train['Fuel'] = X_train['Fuel'].map(mapper_f).fillna(-1).astype(int)
    X_test['Fuel'] = X_test['Fuel'].map(mapper_f).fillna(-1).astype(int)

    return X_train,X_test

X_train,X_test = encoder(X_train,X_test)


model = DecisionTreeRegressor(ccp_alpha=.2)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

tab = pd.DataFrame({'actual':y_test,'predicted':y_pred})

fig = plt.figure(figsize=(20,7),dpi=100)

x_ax = y_test.index
y_act = tab['actual']
y_predicted = tab['predicted']

sns.scatterplot(x=x_ax,y=y_act,color = 'green',label = 'actual')
sns.scatterplot(x=x_ax,y=y_predicted,color = 'red',label='predicted')
for ind,i,j in zip(x_ax,y_act,y_predicted):
    plt.vlines(x=ind,ymin=min(i,j),ymax=max(i,j),color='black', linestyle='--', linewidth=0.5)
plt.title('actual vs predicted')
st.pyplot(fig)

rmse = root_mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
st.write(rmse,r2)

