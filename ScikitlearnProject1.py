#collect training data
#train classifier
#make predictions
from sklearn import tree
features = [[140,1], [130,1], [150,0],[170,0]] #0 bumpy, 1 smooth
labels = [0, 0, 1, 1] # 0  apple, 1 orange
#classifier -> decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[150,0]]))
