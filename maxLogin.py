# Lock account if max login attempts reached
# Brandon Dawson
# 02/06/2024

MAX_LOGIN_ATTEMPTS = 5
correct_password = "password1"

def login():
    attempts = 0
    
    while attempts < MAX_LOGIN_ATTEMPTS:
        login_attempt = input("Enter password: ")
        
        if login_attempt == correct_password:
            print("Login Successful!")
            break
        else:
            attempts += 1
            remaining_attempts = MAX_LOGIN_ATTEMPTS - attempts
            print(f"Incorrect password. {remaining_attempts} attempts remaining.")
            
    if attempts == MAX_LOGIN_ATTEMPTS:
        print("Maximum login attempts reached. Account is locked.")
        
if __name__ == "__main__":
    login()