
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

def split_attributs_target(df):
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    return X,y

def split(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    return X_train, X_test, y_train, y_test

def logistic_regression(X,y):
    X_train, X_test, y_train, y_test = split(X,y)
    #Logistic Regression
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # Summary of the predictions made by the classifier
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    # Accuracy score
    from sklearn.metrics import accuracy_score
    print('accuracy is',accuracy_score(y_pred,y_test))


def Support_Vector_Machine(X,y):
    # Support Vector Machine's
    X_train, X_test, y_train, y_test = split(X,y) 
    from sklearn.svm import SVC

    classifier = SVC()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # Summary of the predictions made by the classifier
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    # Accuracy score
    from sklearn.metrics import accuracy_score
    print('accuracy is',accuracy_score(y_pred,y_test))

def Knearest_neighboors(X,y):
    # K-Nearest Neighbours
    from sklearn.neighbors import KNeighborsClassifier

    classifier = KNeighborsClassifier(n_neighbors=8)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # Summary of the predictions made by the classifier
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    # Accuracy score
    from sklearn.metrics import accuracy_score
    print('accuracy is',accuracy_score(y_pred,y_test))

def Naive_bayes(X,y):
        # Naive Bayes
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # Summary of the predictions made by the classifier
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    # Accuracy score
    from sklearn.metrics import accuracy_score
    print('accuracy is',accuracy_score(y_pred,y_test))

def Decision_Tree(X,y):
        # Decision Tree's
    from sklearn.tree import DecisionTreeClassifier

    classifier = DecisionTreeClassifier()

    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # Summary of the predictions made by the classifier
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    # Accuracy score
    from sklearn.metrics import accuracy_score
    print('accuracy is',accuracy_score(y_pred,y_test))


