import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data.to_dict())

new_data = {row['letter']: row['code'] for (index, row) in data.iterrows()}
print(new_data)


def fetch_word():
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [new_data[name] for name in user_input]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        fetch_word()
    else:
        print(output_list)


fetch_word()