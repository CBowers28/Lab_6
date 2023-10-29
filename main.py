#function is used to print menu and return user input
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    user_choice =int(input("\nPlease enter an option: "))
    return user_choice

def main():
    condition = True
    #While loop runs the program and user choice equals return value from print_menu function
    while condition == True:
        user_choice = print_menu()
        if user_choice == 1:
            #Takes in decoded password and itrates through it adding 3 to each value and then storing it as encoded_password
            decoded_password = input("Please enter your password to encode: ")
            encoded_password = ""
            for char in decoded_password:
                encoded_password_character = int(char)+3
                encoded_password += str(encoded_password_character)
            print("Your password has been encoded and stored!")

        if user_choice == 2:
            orignial_password = ''
            for i in encoded_password:
                new = int(i) - 3
                orignial_password += str(new)
            print(f'The enncoded password is {encoded_password}, and the originnal password is {orignial_password}')


        if user_choice == 3:
            break




if __name__ == "__main__":
    main()

