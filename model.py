#IMPORTING LIBRARIES
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import classification_report
import pandas as pd

#############################################################################

#PREPARING DATA

data = np.loadtxt('data/data.csv', delimiter=',')

X, y = data[:,:-1], data[:, -1]
y = np.array(y)
X  = np.array(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=0)

###########################################################################
#MODELS

models = {
    'knn': KNeighborsClassifier(n_neighbors=10),
    'naive': GaussianNB(),
    'logre': LogisticRegression(C=1e5,solver='lbfgs', multi_class='auto'),
    'linreg': LinearRegression(),
    'svm': SVC(kernel='linear', gamma='auto', C=0.9),
    'tree': DecisionTreeClassifier(max_leaf_nodes=3, random_state=0),
    'random': RandomForestClassifier(n_estimators=100),
    'mlp': MLPClassifier(),
    'lda' : LinearDiscriminantAnalysis()
}

###########################################
#TRAINING SESSION

for md in models:
    model = models[md]
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(y_test)))
    '''print('[**] Using {} model'.format(md))
    print('Train Accuracy: {:.2f}'.format(model.score(X_train, y_train) * 100.0))
    print('Test Accuracy: {:.2f}'.format(model.score(X_test, y_test) * 100.0))
    print('#############################')'''

