from  load_data import load_data
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

def feature_engineering():
    dataset = load_data()

# Finding the duplicate values from the datset
    duplicate = dataset[dataset.duplicated()] 

# Removing the unnecessary features from the dataset
    dataset.drop(columns = 'SI.NO', axis = 1, inplace = True)

# Removing the duplicate columns from the dataset
    for i in duplicate.index:
        print("index", i) 
        dataset.drop(index = [i], inplace = True)
        dataset.reset_index()

# Changing the catregorical values to numerical values
    for col in dataset.select_dtypes(include="object").columns:
        dataset[col] = le.fit_transform(dataset[col])

    return dataset

