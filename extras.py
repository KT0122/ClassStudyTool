import os

def study_topics(path):
    current_topic = open(path)
    
    
def add_topics(class_name):
    print()

def print_topics(class_name):
    path = "./Library/" + class_name
    print (os.listdir(path))

def print_library():
    print (os.listdir("./Library"))

def library():
    print_library()
    while True:
        class_name  = input("Select a clas:\n") 
        try:     
            print_topics(class_name)
            print("1. Add topics")
            print("2. Study topic")
            opt = input()

            if opt == '1':

                continue
            elif opt == '2':
                topic = input("Choose topic:\n")
                study_topics("./Library/" + class_name + "/" + topic)
                continue


        except:
            print("Doesn't exist")
        


def main():
    while True:
        print("1. Access courses")
        print("2. Kill")
        opt = input()

        if opt == '1':
            library()
            continue
        elif opt == '2':
            break
        else:
            print("Try again")