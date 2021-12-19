import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV

# loading dataset
dataframe = pd.read_csv("static/data/spam.csv")
#print(dataframe.describe())

#splitting 80% into training set and 20% into testing set
emailText = dataframe['EmailText']
labels = dataframe['Label']

emailTrain, labelTrain = emailText[0:4457], labels[0:4457]
emailTest, labelTest = emailText[4457:], labels[4457:]

# extract features
cv = CountVectorizer()

## turns string into word counts
features = cv.fit_transform(emailTrain)


# build model

model = svm.SVC()

model.fit(features, labelTrain)
#test accuracy

testFeatures = cv.transform(emailTest)

print("score:", model.score(testFeatures, labelTest))




def _is_string_spam(string):
    transform = cv.transform([string])
    tempresult = model.predict(transform)[0]
    result = tempresult[0:1].upper() + tempresult[1:]
    print(result)
    return(result)

