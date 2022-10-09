from feature_engineering import feature_engineering
from sklearn.model_selection import train_test_split

def pre_processing():
    dataset = feature_engineering()

# setting the variables for dependent variables and independent variable
    x = dataset.drop(['price'], axis = 1)
    y = dataset['price']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state = 0)
    return(x_train, x_test, y_train, y_test)