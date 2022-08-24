import numpy as np
# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")

def handle_missing_values(df):
    perc = 30.0

    min_amount = int(((100-perc)/100)*df.shape[0] +1)
    modified_df = df.dropna(axis=1, thresh=min_amount)
    #print("hello")
    return modified_df
def fill_missing_values(df):

    obj_cols = [col_name for col_name in df.columns.tolist() if df.dtypes[col_name] == object]
    numeric_cols = [col_name for col_name in df.columns.tolist() if col_name not in obj_cols]
    #print(obj_cols)

    #for object type columns use mode
    for col in obj_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    #for numeric type columns use median
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    return df