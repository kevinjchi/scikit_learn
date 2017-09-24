# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:28:02 2017

@author: Chiem PC
"""

from sklearn.datasets import load_iris
iris = load_iris()
#print(iris)
#-----------------description of data
print(iris.keys()) #loads the dictionary

print(iris['data']) #sample data
print(iris['data'].shape)
print(iris['feature_names'])
print(iris["target"]) #target id for each sample
print(iris["target_names"]) #descriptive name for each label

#-----------------data analysis
import numpy as np
import matplotlib.pyplot as plt

x_index = 3
y_index = 1
plt.scatter(iris.data[:,x_index], iris.data[:,y_index],c=iris.target, cmap=plt.cm.get_cmap('RdYlBu', 3))
#label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])
plt.colorbar(ticks=[0,1,2],format=formatter)
plt.clim(-0.5,2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])
#KNN classification
#scikit-learn in 4 steps
#step1 import the class you plan to use
from sklearn.neighbors import KNeighborsClassifier
#step2 Instantiate an Estimator, scikit-learn's term for model
knn = KNeighborsClassifier(n_neighbors=1)
print(knn)
#step3 Model training, fit the model with data. Model is learning the relationship between iris.data and target
knn.fit(iris.data, iris.target)
#step4 predict the response for a new observation
knn.predict([[3, 5, 4, 2],])
#print(iris.target_names[])
#probabilistic predictions:
knn.predict_proba([[3, 5, 4, 2],])
#classification map?
#from fig_code import plot_iris
#plot_iris(knn)

#------------------PCA-dimensionality Reduction:PCA------
"""Principle component analysis (PCA) is a dimension reduction technique in which finds the combinations of variables that explain the most variance"""
import pylab as pl
from sklearn.decomposition import PCA
X, y = iris.data, iris.target
pca = PCA(n_components=2)
pca.fit(X)
X_reduced = pca.transform(X)
print("Reduced dataset shape:", X_reduced.shape)
pl.scatter(X_reduced[:,0], X_reduced[:,1], c=y, cmap='RdYlBu')

print('Meaning of the 2 components:')
for component in pca.components_:
    print("+".join("%.3f x %s" % (value,name)
            for value, name in zip(component,iris.feature_names)))
#--------------------Clustering: K-means
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(X)
y_pred = k_means.predict(X)
pl.scatter(X_reduced[:,0], X_reduced[:,1], c=y_pred, cmap='RdYlBu')
