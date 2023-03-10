import json
def write(val):
 # create a sample dictionary
 usernames = {"last user":val}

 # convert the dictionary to a string
 usernames_str = json.dumps(usernames)

 # write the string to a file
 with open('usernames.json', 'w') as f:
    f.write(usernames_str)

def read():
    # read the string from the file
    with open('usernames.json', 'r') as f:
        usernames_str = f.read()

    # convert the string back to a dictionary
    usernames = json.loads(usernames_str)

    # access the values by key
    return usernames["last user"]  # prints "password1"
