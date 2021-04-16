import() random, string
# set variable, saying it needs to be an integer not a string. must be a numerical response. 
# raw_input asking for user input to return as a string, then convert into an integer
password_length = int(input('\nWhat should the length of the password be?: '))
# variable joining (or concancating three imported strings)
password_characters = string.ascii_letters + string.digits + string.punctuation
# sets a blank list (of strings, individual characters, but strings)
password = []
# saying the script to run 'x' number of times based on the length that the password should be
for x in range(password_length):
    # creating the password from zero (aka adding on to the end of zero)
    password.append(random.choice(password_characters))
# printing the password, taking the list and merges it into a single string
print("Your random password is: ",''.join(password))
