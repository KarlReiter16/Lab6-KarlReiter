def encode(password):
    encoded = ""
    for i in password:
        new_digit = int(i) + 3 #Add 3 to digit
        if (new_digit >= 10):#If the digit rolls over 10
            new_digit -= 10
        encoded += str(new_digit) #Put new digit into the encoded password
    return encoded



if __name__ == '__main__':
    saved_password = ""
    while True:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')
        user_in = int(input("Please enter an option: "))
        if user_in == 1:
            saved_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif user_in == 3:
            break


