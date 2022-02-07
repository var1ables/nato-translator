import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato = {row.letter: row.code for (index, row) in data.iterrows()}

user = input('What do you want translated to nato phonetic?').upper()
answer = [nato[letter] for letter in user]
print(answer)