import pandas as pd

df = pd.read_csv('/mnt/scratch/FA24_CS131_Jessica/jshankarfa24/mini-assignments-jyothi-sh/Shankar-J_A12/crime_test/Crime_Data_from_2020_to_Present.csv')

def remove_null():
    df['Vict Age'] = df['Vict Age'].dropna()
    return (df['Vict Age'].isnull()).sum()


def mean():
    sum = 0
    vict_age = df['Vict Age'].to_list()
    for x in vict_age:
        sum = sum + x
    return sum/len(df['Vict Age'])

def median():
    vict_age_sorted = sorted(df['Vict Age'].to_list())
    if ((len(vict_age_sorted)%2)==0):
        index = (len(vict_age_sorted)+1)/2
        return (vict_age_sorted[index-0.5] + vict_age_sorted[index-1.5])/2
    else: 
        index = int((len(vict_age_sorted)+1)/2)
        return vict_age_sorted[index-1]
