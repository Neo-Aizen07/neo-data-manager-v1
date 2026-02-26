import os
import time
from logger import log_info
from storage import save_names
def clear_proc():
    print("Initialising File Deletion", end='',flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".",end='',flush=True)
def delete_data(record_manager):
        print("Warning: This action will permanently delete your data, Please be sure before proceeding")
        if not record_manager.records:
            print("Error: File is empty")
            log_info("Deletion attempted on empty database", level="WARNING")
            return
        delete_confirm=input("Do you want to proceed with the deletion (Yes/No) :").lower()
        if delete_confirm=="yes":
            print(f"Found Data : {record_manager.display_data()}")
            input_y=input("Is this the data you want to delete (Yes/No) :").lower()
            if input_y=="yes":
                clear_proc()
                try:
                    record_manager.delete_0()
                    print("Your data has been deleted successfully")
                    log_info("All records deleted successfully", level="WARNING")
                except FileNotFoundError as e:
                    print(f"Error: {e}")
                    log_info(f"File not found during deletion: {e}", level="ERROR")
                except Exception as e:
                    print(f"An Unknown Error Occured")
                    log_info(f"ERROR :{e}",level="CRITICAL")
            elif input_y=="no":
                print("Deletion cancelled,Returning to the main menu")
                log_info("Full deletion cancelled by user", level="INFO")
                return
            else:
                print("Data not found, Please Try Again")
                log_info("Data Not Found",level="ERROR")
                return
        if delete_confirm=="no":
            print("Deletion cancelled, Returning to the main menu")
            log_info("Full deletion cancelled by user", level="INFO")
            return
def delete_person(record_manager):
        try:
            name=input("Please enter the username of whose data you want to remove :")
            print("Data present at : ", os.path.abspath(__file__))
            print("Data file name : data.json")
            print(f"Found Data : {record_manager.display_user(name)}")
            input_x=input("Is this the data you want to delete (Yes/No) :").lower()
            if input_x=="yes":
                clear_proc()
                try:
                    record_manager.delete_1(name)
                    print(f"The data of the {name} has been deleted successfully")
                    log_info(f"User deleted: {name}", level="WARNING")
                    print("Returning to main menu")
                    return
                except FileNotFoundError as e:
                    print("No File Found")
                    log_info(f"File Not Found: {e}", level="CRITICAL")
                except Exception as e:
                    print("An Unexpected Error Occured")
                    log_info(f"ERROR : {e}", level="CRITICAL")
            elif input_x=="no":
                print("Deletion cancelled, Returning to main menu")
                log_info(f"User deletion cancelled: {name}", level="INFO")
                return
            else:
                print("Please enter a valid input, Returning to main menu")
                return
        except FileNotFoundError as e:
            print(f"File not found")
            log_info(f"User not found during deletion: {e}", level="ERROR")
        except Exception as e:
            print("An Unknown Error Occured")
            log_info(f"ERROR : {e}", level="CRITICAL")