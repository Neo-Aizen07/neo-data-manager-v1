from storage import file_load
import uuid
import time
from logger import log_info
def search_func(record_manager):
    input_1=input("Do you want to search using ID or Username:").lower()
    found=False
    if input_1=="id":
        search_id(record_manager)
    elif input_1=="username":
        search_username(record_manager)
    else:
        print("Please enter a valid entry and try again")
        log_info(f"Invalid search type: {input_1}", level="WARNING")
        return
def search_id(record_manager):
    enter_id=input("Please enter your ID to search :")
    found=False
    for user,details in record_manager.records.items():
        if details["ID"] == enter_id:
            username=user
            name=details.get("Name")
            uid=details.get("ID")
            last=details.get("Last Saved")
            print(f"Username : {username} \n Name : {name}\n ID : {uid}\n Last Saved : {last}")
            log_info(f"ID search successful: {enter_id}", level="INFO")
            found=True
            break
    if not found:
        print("ID not found, Try Again")
        log_info(f"ID search no results: {enter_id}", level="WARNING")
        return
def search_username(record_manager):
    partial_input=input("Please enter your username to search :")
    matches=[i for i in record_manager.records if partial_input in i]
    if not matches:
        print("No data Found")
        log_info(f"Username search no results: {partial_input}", level="WARNING")
        return
    else:
        print(f"Found {len(matches)} usernames")
        log_info(f"Username search successful: {result}", level="INFO")
        for index,user in enumerate(matches,start=1):
            print(f"{index} : {user}")
        try:
            result=input("Please type the username you want the details about from the list above :").lower().strip()
            if result in record_manager.records:
                data=record_manager.records[result]
                username=result
                name=data.get("Name")
                uid=data.get("ID")
                last=data.get("Last Saved")
                print(f"Username : {username} \n Name : {name}\n ID : {uid}\n Last Saved : {last}")
                log_info(f"Username search successful: {result}", level="INFO")
            else:
                print("Username not found, Try Again")
                log_info(f"Username search unsuccessful: {result}", level="INFO")
        except Exception as e:
            print(f"An Unexpected Error Occured")
            log_info(f"ERROR : {e}", level="ERROR")