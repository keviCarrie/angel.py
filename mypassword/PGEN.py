#Password Generator
import random
# List of the different Characters types for creating passwords

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+']

all_keys = letters + capital_letters + numbers + symbols

print("Welcome to MyPassword Generator! \nThis tool will generate a random password that includes uppercase letters, lowercase letters, numbers, and symbols")

#Different platforms requir different minimum character password length and might have different maximums. 
#the following prompt is for the user

min_input = int(input("What is the minimum number of characters your password should be? "))
max_input = int(input("What is the maximum number of characters your password should be? "))

# randomly select a password length between the min and max number of characters 

password_length = (random.choice(range(min_input, max_input + 1)))

# A blank list to generate the password into
password = []

#Add one of each character type
#some applications require passwords to include atleast one uppercase letter, lowercase letter, symbol and number 
#adding one of each will meet the minimum requirements 

password.append(random.choice(letters))
password.append(random.choice(capital_letters))
password.append(random.choice(numbers))
password.append(random.choice(symbols))

# Add in random characters from each type to populate the remainder of the password
for i in range(1, password_length - 3):
    if len(password) < password_length:
        password.append(random.choice(all_keys))
#shuffle the password list to randomize it.
    random.shuffle(password) 
#concatenate the individual characters in the password list into a string with the join function

    final_random_password = ''.join(password) 
    print (f"Your password is: {final_random_password}")          