import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint as sp_randInt
from scipy.stats import uniform as sp_randFloat
from sklearn import metrics

class GradientBoostingRegression:
    def getName(self):
        return "Gradient Boosting Regression"

    def gridSearch(self,model,X_train,y_train):

        param_grid = {}

        randm = RandomizedSearchCV(estimator=model, param_distributions = param_grid,
                                  cv = 5, n_iter = 5, n_jobs=5)
        randm.fit(X_train, y_train)

        #Results from Random Search
        print("\n========================================================")
        print(" Results from grid Search ")
        print("========================================================")

        print("\n s:\n", randm.best_estimator_)

        print("\n The best score across ALL searched params:\n", randm.best_score_)

        print("\n The best parameters across ALL searched params:\n",randm.best_params_)

        clf = GradientBoostingRegressor(tol=0.001,n_estimators=10,random_state=42,verbose=1)

        return clf

    def run(self,trainingDasaset,plotting):
        dataset = trainingDasaset
        accuracy = 0
        y = dataset['int_rate']
        X = dataset.drop(columns=['int_rate',])
        if plotting==True:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
            clf = GradientBoostingRegressor(tol=0.001,n_estimators=10,random_state=42,verbose=1)
            #clf=self.gridSearch(clf,X_train, y_train)
            clf.fit(X_train, y_train)
            print("###################################GradientBoostingRegressor#############################")
            accuracy=clf.score(X_test, y_test)
            #pred = clf.predict(X_test)
            #accuracy = np.sqrt(metrics.mean_squared_error(y_test,pred))
            print("score:"+str(accuracy))

        else:
            clf = GradientBoostingRegressor(tol=0.001,n_estimators=10,random_state=42,verbose=1)
            #clf=self.gridSearch(clf,X_train, y_train)
            clf.fit(X, y)
            testData = pd.read_csv("./SiameseNeuralNetworkProject/MachineLearningAlgorithmSuite/CleanedData/SiameseTrainingData.csv")
            predictions = clf.predict(testData)
            np.savetxt("./SiameseNeuralNetworkProject/MachineLearningAlgorithmSuite/OutputFiles/GradientBoostingRegressorPredictions.csv", predictions, delimiter=",")

            testData = pd.read_csv("./SiameseNeuralNetworkProject/MachineLearningAlgorithmSuite/CleanedData/OverallTestingData.csv")
            predictions = clf.predict(testData)
            np.savetxt("./SiameseNeuralNetworkProject/MachineLearningAlgorithmSuite/OutputFiles/GradientBoostingRegressorPredictionsTestData.csv", predictions, delimiter=",")

        return accuracy
