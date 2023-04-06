from pprint import pprint
import requests
import json
import time

# The request is filtered to include the body of the question into the response


def get_database_of_questions():
    unix_current_timestamp = int(time.time())
    unix_dby_timestamp = unix_current_timestamp - 172800
    url = f"https://api.stackexchange.com/2.3/questions?order=desc&min={unix_dby_timestamp}&max={unix_current_timestamp}&sort=activity&tagged=Python&site=stackoverflow&filter=!)riR7Z9)aTf2rIvk7*_b"
    response = requests.get(url)
    questions = response.json()
    Stack_questions_dictionary = {}
    for item in questions['items']:
        Stack_questions_dictionary[item['title']] = [item['link'], item['body']]
    return Stack_questions_dictionary


# Option 1. Prints the list to the json-file
def write_to_json(Stack_questions_dictionary):
    with open("Full_list_of_questions.json", "w") as file:
        json.dump(Stack_questions_dictionary, file, indent = 2)
        print("json-file is ready")
    return


# Option 2. Print the list to the txt.file
def write_to_txt(Stack_questions_dictionary):
    with open("list_of_questions.txt", "a", encoding='utf-8') as file:
        for no, title in enumerate(Stack_questions_dictionary):
            file.write(f"{no+1}. {title}\n")
            # Prints the link to the question
            file.write(f"{Stack_questions_dictionary[title][0]}\n")
            # for printing the text of the question as well
            # file.write(f"{Stack_questions_dictionary[title][1]}\n")
        print("txt-file is ready")
    return

if __name__ == '__main__':
    write_to_json(get_database_of_questions())
    write_to_txt(get_database_of_questions())








