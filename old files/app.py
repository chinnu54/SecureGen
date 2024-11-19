import random,string


def GeneratePassword():
    letters=list(string.ascii_lowercase)+list(string.ascii_uppercase)
    #stored all alpha characters


    special_characters=list(string.punctuation)#storing all special character to generate a strong unbreakable passowrd
    # print(special_characters)


    numbers=list("1234567890")#string all single digit numbers
    # print(numbers)

    # procedure for to generate alpha numeric character passwrd including special characters


    try :
        n_letters=int(input("Enter count of alphabets that you want in  your password:"))
        n_numbers=int(input("Enter count of digits(0-9) that you want in  your password:"))
        n_special_characters=int(input("Enter count of special characters that you want in  your password:"))
        # note all special characters included




    except ValueError:
        # print("Invalid input\n",ValueError)
        return "V"


    if(n_letters <0 or n_numbers <0 or n_special_characters<0):
        # print("Counts cannot be negative ...Try again!")
        return "N"


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

if __name__=="__main__":
    passowrd=GeneratePassword()
    if passowrd:
        if passowrd=="V":
            print("\n****please Enter  valid values as a Input(only positive integer values are accepted )****")
            print("Try again !")

        elif passowrd=="N":
            print("You entered negative values...Try again")
        else:
            print("Generated Password is",passowrd)
    else:
        print("Something get's wrong ...please try again after some time!")