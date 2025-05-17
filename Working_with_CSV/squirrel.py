import pandas as pd

data = pd.read_csv('Squirrel-Census-Squirrel-Data.csv')
grey_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])
# print(grey_squirrel)

data_dict = {
    "Fur Color": ['Grey', 'Cinnamon', 'Black'],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}
#
squirrel = pd.DataFrame(data_dict)
squirrel.to_csv('squirrel_count.csv')