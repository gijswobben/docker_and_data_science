# Imports
import pickle

from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


# Load the Iris dataset from sklearn
dataset = datasets.load_iris()

# Create a decision tree and fit it to the data
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)

# Make some predictions for evaluation of the model
expected = dataset.target
predicted = model.predict(dataset.data)
print(dataset.data)

# Evaluate the models performance
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

# Store the model for later use
pickle.dump(model, open('models/iris_classifier.pickle', 'wb'))
