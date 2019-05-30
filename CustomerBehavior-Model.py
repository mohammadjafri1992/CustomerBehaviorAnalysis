# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:39:17 2019

@author: muham
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time


dataset = pd.read_csv('my_new_appdata10.csv')

# DATA PRE-PROCESSING

# Since our response variable is whether the user enrolled in our premium offering
# or not, therefore from the dataset, the name of the columns which tells us 
# this information is 'enrolled'. So we create a variable called "response"
# which holds that information, and we drop this column from our dataset.

response = dataset['enrolled']
dataset = dataset.drop(columns = ['enrolled'])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(dataset, response,
                                                    test_size = 0.2,
                                                    random_state = 0)

train_identifier = X_train['user']
X_train = X_train.drop(columns='user')
test_identifier = X_test['user']
X_test = X_test.drop(columns='user')

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()

# fit_transform first fits the data (X_train and y_train) to the model
# and then returns a transformed version (i.e. a standardized version)

X_train2 = pd.DataFrame(sc_X.fit_transform(X_train))

# Using only transform gives us the standardized version of X_test
X_test2 = pd.DataFrame(sc_X.transform(X_test))

X_train2.columns = X_train.columns.values
X_test2.columns = X_test.columns.values
X_train2.index = X_train.index.values
X_test2.index = X_test.index.values
X_train = X_train2
X_test = X_test2


# Model Building
# In this step, we build our final model.

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state = 0, penalty = 'l1')

# The reason why we create a random_state and penalty here is that 
# if we want to use this classifier anywhere else, we will not have to
# specify these values again. This however restrics our ability to 
# tune each model a little bit, but that does;nt really matter here.

# We are using L1 Regularization here because L1 regularization penalizes
# the variables whcich get a really big co-efficient (high correlation)
# with the output variable (i.e. the target variable, 'screens' in our case).

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)


# Now, in order to check how accurate our model was, we shall 
# perform some analytics using built-in modules from sklearn.metrics.
# as shown below.

from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score

cm = confusion_matrix(y_test, y_pred)
accuracy_score(y_test, y_pred)
precision_score(y_test, y_pred)

# Precision tells us about how precise our model was in guessing the
# positives. 
# Precision = (True positives) / (True Positives + False Positives)

recall_score(y_test, y_pred)
# Recall = (True Positives) / (True Positives + False Negatives)

f1_score(y_test, y_pred)

# After considering all True/False positives and all True/False Negatives,
# we shall generate our F1-Score.


df_cm = pd.DataFrame(cm, index = (0, 1), columns = (0, 1))
plt.figure(figsize = (10,7))
sns.set(font_scale=1.4)
sns.heatmap(df_cm, annot=True, fmt='g')
print("Test Data Accuracy: %0.4f" % accuracy_score(y_test, y_pred))

# Using k-fold cross-validation

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10)
print("Logistic Regression Accuracy: %0.3f (+/- %0.3f)" % (accuracies.mean(), accuracies.std() * 2))


# Formatting the results

final_results = pd.concat([y_test, test_identifier], axis=1).dropna()

# Remember, that variable 'test_identifier' has already been defined above
# and it is 'users' column from X_test dataset

final_results['predicted_results'] = y_pred
final_results[['user','enrolled','predicted_results']].reset_index(drop=True)

# The above process of 'visualizing' the final result will make us 
# understand the whole process even better./
# If we have this data available, then the users who are likely 
# to subscrive and have not subscribed yet, we can offer them some 
# extra perks to make them join the premium program. e.g. American Express
# first sends you the Gold card offers for 5-8 months, and if you have a good
# credit, and still haven't signed up for the Gold card, they offer you 
# Platinum card with even more perks.

# The model we created lays the groundwork for similar business models / subscription services
# so that we can craft a unique proposal for individual customers.














