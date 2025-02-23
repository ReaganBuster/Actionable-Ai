import os
 
def fetch_file(file_name) ->  str:
    if os.path.exists(f"{file_name}.txt"):
        with open(f"{file_name}.txt", "r") as file:
            return file.read()
    else:
        print("File not found!")

def fetch_goal()-> str:
    return fetch_file("prompt")
    
def fetch_reviews() -> str:
    return fetch_file('reviews')
    
def fetch_business_data() -> str:
    return fetch_file('business_data')
    