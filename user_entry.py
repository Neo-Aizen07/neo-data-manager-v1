import os
import datetime
import uuid
from storage import save_names
from user_interface import time_save, generate_id
from logger import log_info
from Validation import user_valid,name_valid
def name_enter(record_manager):
    try:
        print("The data will be stores locally on ", os.path.abspath(__file__))
        print("NOTE : Usermane must contain 3 min characters and max 20 characters,only 4 Special Characters are allowed")
        username=input("Please enter a username :").strip()
        if not user_valid(record_manager,username):
            log_info(f"Invalid username attempt: {username}", level="WARNING")
            return
        print("NOTE : The name will be used only for the display purpose")
        name_first=input("Please enter your first name :").strip()
        name_last=input("Please enter your Last name (optional if exsists):").strip()
        if username in record_manager.records:
            print("Username already exists, Please Try Again")
            return
        if not name_valid(name_first,name_last):
            log_info(f"Invalid name entry for: {username}", level="WARNING")
            return
        name=(name_first+" "+name_last).strip()
        record_manager.update_record(username,name,generate_id(),time_save())
        print("Registration Successful!")
        log_info(f"Registration successful: {username}", level="INFO")
        return
    except Exception as e:
        print("An Unexpected Error Occured")
        log_info(f"ERROR : {e}",level="CRITICAL")