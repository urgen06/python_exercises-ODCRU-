import getpass

username = "urgen12"
password = "urgen@123"

attempt = 0

for x in range(3):
    input_username = input("Username: ")
    input_password = getpass.getpass("Password: ")

    if username == input_username and password == input_password:
        print("Success!! You have logged in succesfully.")
        break
    
    else:
        attempt += 1
        remaining = 3 - attempt
        print(f"Wrong credentials. Remaining attempts: {remaining}")
else:
    print("You have been locked! Please wait")