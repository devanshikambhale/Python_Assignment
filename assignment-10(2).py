# Create a table showing information about 5 states such as:
# a) Name of the state
# b) Area
# c) Population

# Generate the following reports:
# a) Print the complete information of states
# b) Print the name of the State having largest Area
# c) Print the name of State having largest population
# d) Create a mechanism to calculate the population density of States
# e) Determine the name of State with highest population density
import pandas as pd

state = ['S1','S2','S3','S4','S5']
area = [100000,150000,90000,120000,110000]
pop = [5000000,8000000,3000000,7000000,6000000]

df = pd.DataFrame(list(zip(state, area, pop)), columns=['State','Area','Population'])

print(df)

print(df.loc[df['Area'].idxmax(), 'State'])
print(df.loc[df['Population'].idxmax(), 'State'])

df['Density'] = df['Population'] / df['Area']
print(df)

print(df.loc[df['Density'].idxmax(), 'State'])