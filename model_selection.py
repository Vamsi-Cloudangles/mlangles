from pre_processing import pre_processing
import sklearn.linear_model as sl
lr = sl.LinearRegression()
import sklearn.tree as tree
dtr = tree.DecisionTreeRegressor()
import sklearn.ensemble as se
rfr = se.RandomForestRegressor(random_state = 42)
import sklearn.metrics as mt
import math
import pickle

def model_selction():
    x_train, x_test, y_train, y_test = pre_processing()
    score = []
    model = [lr, dtr, rfr]
    
    lr.fit(x_train,y_train)
    lrs = lr.score(x_test, y_test)
    score.append(lrs)

    dtr.fit(x_train,y_train)
    dtrs = dtr.score(x_test, y_test)
    score.append(dtrs)

    rfr.fit(x_train,y_train)
    rfrs = rfr.score(x_test, y_test)
    score.append(rfrs)

    max_score = max(score)
    for i in range(len(score)):
        if score[i] == max_score :
            best_model = model[i] 

    y_predict = best_model.predict(x_test)
    MSE = mt.mean_squared_error(y_test, y_predict)
    RMSE = math.sqrt(MSE)
    MAE = mt.mean_absolute_error(y_test,y_predict)
    
    with open("dimond_pickle.pkl", 'wb') as p:
     pickle.dump(model,p)       
    return(MSE, RMSE, MAE)