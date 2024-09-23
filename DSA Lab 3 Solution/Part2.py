import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# Task 01: Load the dataset
train_df = pd.read_csv('Data/Train.csv')
test_df = pd.read_csv('Data/Test.csv')  # Assuming 'Test.csv' is loaded here

# Task 02: Scatter plots for each symptom against the label
symptoms = train_df.columns[:-1]  # All columns except 'TYPE'
for symptom in symptoms:
    plt.scatter(train_df[symptom], train_df['TYPE'])
    plt.title(f"{symptom} vs Label")
    plt.xlabel(symptom)
    plt.ylabel('TYPE')
    plt.show()

