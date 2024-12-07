import pandas as pd

df = pd.read_csv('/mnt/scratch/FA24_CS131_Jessica/jshankarfa24/mini-assignments-jyothi-sh/Shankar-J_A12/crime_test/Crime_Data_from_2020_to_Present.csv')


def vict_sex_column_check():
    if (((df['Vict Sex'].isnull()).any()) & (~((df['Vict Sex'].isin(['M','W'])).any()))):
        return "Column Contains Null Values and values that are not M or W"
    elif ((df['Vict Sex'].isnull()).any()):
        return "Column Contains Null Values"
    elif (~((df['Vict Sex'].isin(['M','W'])).any())):
        return "Column contains values that are not M or W"
    else:
        return "Column values are Clean"

def vict_age_column_check():
    if (((df['Vict Age'].isnull()).any()) & (((1 > df['Vict Age']) | (df['Vict Age'] > 100)).any())):
        return "Column containes null values and invalid age values"
    elif ((df['Vict Age'].isnull()).any()):
        return "Column Contains Null Values"
    elif (((1 > df['Vict Age']) | (df['Vict Age'] > 100)).any()):
        return "Column contains invalid age value"
    else:
        return "Column values are Clean"

def type_check():
    if (df['Vict Sex'].dtype != object):
        return "Incorrect Column Type"
    elif (df['Vict Age'].dtype != int):
        return "Incorrect Column Type"
    else:
        return "Types are Correct"
