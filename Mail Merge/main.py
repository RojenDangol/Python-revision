REPLACE_NAME = '[name]'

with open('Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()

with open('Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

    for name in names:
        stripped_names = name.strip()
        new_letter = letter.replace(REPLACE_NAME, name)
        with open(f'Output/ReadyToSend/letter_for_{stripped_names}.txt', 'w') as send_file:
            send_file.write(new_letter)
