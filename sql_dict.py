import mysql.connector
from difflib import get_close_matches

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = conn.cursor()
usr = input("Please enter a word: ")

cursor.execute("SELECT Expression FROM Dictionary")
terms = [term[0] for term in cursor.fetchall()]

cursor.execute('SELECT * FROM Dictionary')
# the above query returns a list of tuples, e.g. [('word1', 'definition'), ('word2', 'definition')]
# we want to turn this into a dictionary, e.g. {'word1': 'definition', 'word2': 'definition'}
dictionary = dict((x,y) for x,y in cursor.fetchall())

def search(word):
    """"""
    word = word.lower()
    if word in terms:
        return dictionary[word]
    elif len(get_close_matches(word, terms)) > 0:
        choice = input(f"Did you mean {get_close_matches(word, terms)[0]}?(Y/N): ")
        if choice == 'Y':
            return dictionary[get_close_matches(word, dictionary.keys())[0]]
        else:
            return "Choose a different word."
    else:
        print("No word found!")

print(search(usr))