def user_valid(record_manager,username):
    SPECIAL_CHAR="'!_-@#$%^&*()+=[]{}|;:,.<>?/`~"
    count=sum(1 for char in username if char in SPECIAL_CHAR)
    if username in record_manager.records:
        print("Username Already Exists, Please Try Again")
        return False
    if username.lower()!=username:
        print("Username must not contain any uppercase letters")
        return False
    if len(username)<3 or len(username)>=20:
        print("Invalid Number of Characters in username")
        return False
    elif not username:
        print("Invalid input, Username cannot be empty. Please try again.")
        return False
    elif count>=4:
        print("Invaid Input, Exceeds the number of Special Characters")
        return False
    elif " " in username:
        print("No spaces allowed in Username")
        return False
    return True
def name_valid(name_first,name_last):
    if not name_first:
        print("Invalid input, Name cannot be empty. Please try again.")
        return False
    elif not name_first.isalpha():
        print("Invalid input, Name cannot contain numbers or special characters. Please try again.")
        return False
    elif " " in name_first:
        print("Invalid input, Name cannot contain spaces. Please try again.")
        return False
    if name_last and not name_last.isalpha():
        print("Invalid input, Name cannot contain numbers or special characters. Please try again.")
        return False
    if " " in name_last:
        print("Invalid input, Name cannot contain spaces. Please try again.")
        return False
    return True
    