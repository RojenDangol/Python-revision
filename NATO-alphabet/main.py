import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data.to_dict())

new_data = {row['letter']: row['code'] for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
output_list = [new_data[name] for name in user_input]
print(output_list)
