
# passward strength Checker 
import re

# Strength check condition
def check_password_strength(password):
    if len(password) < 8:  # Length check
        return "Weak: Password must be at least 8 characters long"
    
    if not any(char.isdigit() for char in password):  # Check for digits
        return "Weak: Password must contain at least one digit"
    
    if not any(char.isupper() for char in password):  # Check for uppercase letters
        return "Weak: Password must contain at least one uppercase letter"
   
    if not any(char.islower() for char in password):  # Check for lowercase letters
        return "Weak: Password must contain at least one lowercase letter"

    if not re.search(r'[!@#$%^&*]', password):  # Check for special characters
        return "Weak: Password must contain at least one special character (!@#$%^&*)"
    
    return "Strong: Your password is strong"

def password_checker():
    print("Welcome to the password checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
    
        if password.lower() == 'exit':
            print("Thank you for using this tool.")
            break
        
        result = check_password_strength(password)
        print(result)

# Run the checker tool
if __name__ == "__main__":
    password_checker()



