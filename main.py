import pandas


def generate():
    data = pandas.read_csv('nato_phonetic_alphabet.csv')
    nato = {row.letter: row.code for (index, row) in data.iterrows()}

    user = input('What do you want translated to nato phonetic?').upper()
    try:
        answer = [nato[letter] for letter in user]
    except KeyError:
        print('Only letters please')
        generate()
    else:
        print(answer)

generate()