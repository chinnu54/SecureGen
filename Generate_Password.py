import random,string


def GeneratePassword(n_letters,n_numbers,n_special_characters):
    letters=list(string.ascii_lowercase)+list(string.ascii_uppercase)
    #stored all alpha characters


    special_characters=list(string.punctuation)#storing all special character to generate a strong unbreakable passowrd
    # print(special_characters)


    numbers=list("1234567890")#string all single digit numbers
    # print(numbers)

    # procedure for to generate alpha numeric character passwrd including special characters

    password_characters=[]
    lengthOfPassword=n_letters+n_numbers+n_special_characters
    for i in range(0,lengthOfPassword):


        if(i<n_letters):
            # choosing alphabets
            password_characters+=random.choice(letters)
        elif(i<n_letters+n_numbers):
            # choosing digits
            password_characters+=random.choice(numbers)
        else:
            # choosing special symbols
            password_characters+=random.choice(special_characters)


    # print(password_characters)
    random.shuffle(password_characters)
    # print(password_characters)
    password=""
    for char in password_characters:
        password+=char
    return password