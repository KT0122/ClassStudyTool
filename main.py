import os
import random

# Start studying
def study_topics(path):
    # Variable setup
    study_dict = {}
    current_topic = open(path, encoding="utf-8")
    lines = current_topic.readlines()

    # Go line by line
    for line in lines:
        # Split and strip the line
        line = line.strip().split(", ")

        # Add lines to the dictionary
        study_dict[line[0]] = line[1::]

    # Save the keys in a list, create a used key list
    dict_keys = list(study_dict.keys())
    used_keys = []
    studying = True

    while studying:
        # Shuffle the dict, pop the fron key, save it to used, and grab the answer
        random.shuffle(dict_keys)
        current = dict_keys.pop()
        used_keys.append(current)
        answer = study_dict[current]

        # While the user hasn't gotten the answer right, propmt them and check the answer
        while True:
            prompt = "What is the Hiragana for " +  current + "?\n"
            user_answer = input(prompt).lower()
           
            # Compare the user's answers to the actual answer and respond appropriately
            if user_answer == answer[0]:
                print("Correct")
                # If there is a kanji character print it too
                if len(answer) == 2:
                    print("The kanji for this character is: ", answer[1])
                break
            # Set the studying flag to false and break out of inner while loop if quit
            elif user_answer == "quit":
                studying = False
                break
            else:
                print("Try again")
                continue


# List potential topics to study from
def main():
    # Print all topics in the current library
    print(os.listdir("./Library/JP"))

    # Propmt users for input 
    topic = input()

    # Pass input to study topics method
    study_topics("./Library/JP/" + topic)

if __name__ == '__main__':
    main()
