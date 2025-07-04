import json

bible_word_dict = {}

def parse_word_dict():
    global bible_word_dict
    with open("data/bible_word_dictionary.txt", "r") as file:
        bible_word_dict = json.loads(file.read())

def main():
    parse_word_dict()
    while True:
        word = input("What word (q=quit)? ").lower()
        if word == "q":
            break
        print("\"" + word + "\" appears " + str(bible_word_dict[word]) + " times." if word in bible_word_dict else "\"" + word + "\" is not in the bible")

if __name__ == "__main__":
    main()