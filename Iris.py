from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle as pickle
import streamlit as st

st.title('Iris')

iris = load_iris()
X, y = iris.data, iris.target


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(y_train.shape)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

print("Scroring model to pickle file")
pickle.dump(clf,open("iris_model.pkl", 'wb'))

st.write(X_train)
