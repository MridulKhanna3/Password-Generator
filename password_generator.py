import secrets
import string
import random

print("Welcome to password manager!")
saveaccess_password = input("Do you want to save or have access to your passwords?(yes or no): ").lower()

if saveaccess_password == "yes":
    # code to save the password (password manager tutorial goes here)
    
    def view():
        with open("passwords.txt","r") as f: #w mode to overide the existing file, r mode to read the file, a mode is append mode that lets to add to the existing file, and if that file doesnt exist it will create a new file for it
            for line in f.readlines():
                data = line.rstrip()
                application, user, passw = data.split("|")
                print("Application: ", application, " ,User: ", user, " ,Password: ", passw)

    def generate():
        website = input("what website is this password for? ")
        name = input("Account Name: ")
        password_len = int(input("how long do you want the password? "))

        specific_word1 = input("Please enter 1 word that you want in the password: ")

        letters = ""
        letters_need = input("Do you want letters in the password? ").lower()
        if letters_need == "yes":
            letters = string.ascii_letters

        digits = ""
        digits_need = input("Do you want digits in the password? ").lower()
        if digits_need == "yes":
            digits = string.digits

        special_chars = ""
        special_chars_need = input("Do you want special characters in the password? ").lower()
        if special_chars_need == 'yes':
            special_chars = string.punctuation


        selection_list = letters + digits + special_chars  

        password_list = [specific_word1]

        password = " "    
        for i in range(password_len-len(specific_word1)):
            password += ''.join(secrets.choice(selection_list))

        password_list.append(password)

        random_number = random.randint(0,password_len) #whatever the random number is, the specific word gets put in there

        password_final = password[:random_number] + specific_word1 + password[random_number:]

        print(f"here is your password: {password_final}")
        pwd = password_final

        save_password = input("Do you want to save this password?: ").lower()
        if save_password == "yes":
            with open("passwords.txt","a") as f: #w mode to overide the existing file, r mode to read the file, a mode is append mode that lets to add to the existing file, and if that file doesnt exist it will create a new file for it
                f.write(website + "|" + name + "|" + pwd + "\n") 
        else:
            pass

    def add():
        website = input("what website is this password for? ")
        name = input("Account Name: ")
        pwd = input("What is the password? ")
        with open("passwords.txt","a") as f: #w mode to overide the existing file, r mode to read the file, a mode is append mode that lets to add to the existing file, and if that file doesnt exist it will create a new file for it
                f.write(website + "|" + name + "|" + pwd + "\n") 


    while True:
        mode = input("Would you like to generate a new password or view an existing one? (view, generate), press q to quit: ")
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "generate":
            generate()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue 
else:
    print("Thank You for using our program!")
