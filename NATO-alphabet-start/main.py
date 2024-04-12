student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        userInput = input("enter word: ").upper()
        userInput = userInput.replace(" ", "")
        uin = [letter for letter in userInput]
        result = [nato[letter] for letter in uin]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break


print(result)
