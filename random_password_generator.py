
import secrets

print ("Welcome to your psssword generator")

while True:
    try:
        pass_len = int(input("How long should your password be? " ))

        if pass_len <= 0:
            print ("Enter a number greater than 0.")
            continue
        break
    
    except ValueError:
        print("Invalid Input; Enter a positive number")
    
    
count = 0

password = ""


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?_-+()/%"

while count < pass_len:
    
    password += secrets.choice(characters)
    
    count += 1
    


print ("Your password is: " + password)