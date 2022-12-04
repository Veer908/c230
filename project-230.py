import pandas as pd

dataset = pd.read_csv(r'country_vaccinations.csv')
print("Shape of the given dataset", dataset.shape)
print("Columns" len(dataset.column))
print("Name of parameter used:",dataset.columns)
