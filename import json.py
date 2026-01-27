import json
import sys
import qrcode
import time
import datetime
import os
import uuid
class NameManager():
    def __init__(self): 
        self.name_folder_1={}
        self.file_load(silent=True)
    def clear_menu(self):
        command=("cls"if os.name=="nt" else "clear")
        os.system(command)
        print("*" *50)
    def file_intro(self):
        print("-"*50)
        print("WELCOME TO DATABASE MANAGEMENT SYSTEM (JSON Based)")
        print("Version v1.0.0")
        print("-"*50)
    def name_enter(self):
        name=input("Please enter your name :")
        if not name.replace(".","").replace(" ","").isalpha(): #this is added to to allow spaces and dots in names to reduce the invalid name entries and make it more user friendly
            print("Invalid name, Please try again")
            return
        if name not in self.name_folder_1:
            self.name_folder_1[name]={"ID" : self.id_save(), "Last saved" : self.time_save()}
            self.save_names()
            print("Name and Unique ID added successfully")
        else:
            print("Name already exists, Please try again")
        return self.name_folder_1
    def time_save(self):
        time=datetime.datetime.now().isoformat(timespec="seconds")
        iso_time=str(time.replace("T","/"))
        return iso_time
    def id_save(self):
        id=uuid.uuid4().hex[:10]
        id_1=str(id)
        return id_1
    def del_data(self):
        user_folder=self.name_folder_1
        delete=input("Do you wanna delete the entire data(enter 'entire data' or '0') or just a particular person's data (enter 'person' or '1') (Note: It is a permanent deletion, no way to recover the deleted data) :").lower()
        if delete=="entire data":
            print(f"Found Data :{user_folder}")
            input_y=input("Is this the data you want to delete (Yes/No) :").lower()
            if input_y=="yes":
                print("Initialising File Deletion", end='',flush=True)
                for i in range(3):
                    time.sleep(0.5)
                    print(".",end='',flush=True)
                try:
                    self.name_folder_1.clear()
                    self.save_names()
                    print("Your data has been deleted entirely")
                except FileNotFoundError:
                    print("No data exists")
                except Exception as e:
                    print("An Unknown Error Occured, {e}")
                    raise
            elif input_y=="no":
                print("Deletion cancelled,Returning to the main menu")
                return
            else:
                print("Data not found, Please Try Again")
        elif delete=="person":
            try:
                name=input("Please enter the name of whose data you want to remove :")
                if name in user_folder:
                    print(f"Found Data :{user_folder[name]}")
                    input_x=input("Is this the data you want to delete (Yes/No) :").lower()
                    if input_x=="yes":
                        print("Initialising File Deletion", end='',flush=True)
                        for i in range(3):
                            time.sleep(0.5)
                            print(".",end='',flush=True)
                        try:
                            self.name_folder_1[name].clear()
                            self.save_names()
                            print(f"The data of the {name} has been deleted successfully")
                            print("Returning to main menu")
                        except FileNotFoundError:
                            print("No data exists")
                        except Exception as e:
                            print("An Unknown Error Occured, {e}")
                            raise
                    elif input_x=="no":
                        print("Deletion cancelled, Returning to main menu")
                        return
                    else:
                        print("Please enter a valid input, Returning to main menu")
                        return
                elif name not in user_folder:
                    print("Name not found, Try Again")
                else:
                    print("Invalid Input, Try Again")
            except FileNotFoundError:
                print("Name not found, Try Again")
    def search_name(self): # This function is used to search for a name and know whether it exists or not
        input_1=input("Do you want to search using ID or Name :").lower()
        if input_1=="name":
                found=False
                name=input("Please enter your name to search :")
                if name in self.name_folder_1:
                    user_input=self.name_folder_1[name]
                    print(f"Name :", name)
                    print("Unique ID found :",user_input.get("ID"))
                    print(f"Last saved time :{user_input.get('Last saved')}")
                    found=True
                    if not found:
                        print("ID not found, Try Again")
        elif input_1=="id":
            id=input("Please enter your ID to search :")
            found=False
            for name,data in self.name_folder_1.items():
                if data["ID"] == id:
                    print(f"Name :", name)
                    print("Unique ID found :",data.get("ID"))
                    print(f"Last saved time :{data.get('Last saved')}")
                    found=True
                if not found:
                    print("ID not found, Try Again")
        else:
            print("Please enter a valid name or entry and try again")
            self.enter_direct
    def enter_direct(self):
        input_1=input("Do you want to open the file now ? (yes/no)").lower()
        if input()=="yes":
                self.file_load()
        elif input()=="no":
            print("Okay, Returning to main menu")
            return
        else:
            print("Invalid input, Returning to main menu")
    def save_names(self): # This function is used to save the names to a json file and handle permission errors
        try:
            with open ("lost.json", "w") as f:
                json.dump(self.name_folder_1,f)
        except PermissionError:
            print("Permission denied, cannot save the file")
            return
        except json.JSONDecodeError:
            print("Error encoding JSON, Please try again")
            return
    def file_load(self,silent=False):
        try:
            with open("lost.json","r") as f:
                name_folder_dict=json.load(f)
                self.name_folder_1=name_folder_dict
                if not silent:
                    print("Loaded Names:")
                    for name in self.name_folder_1:
                        duplicate=self.name_folder_1[name]
                        print("Your name is :",name)
                        print("Your unique ID is :",duplicate["ID"])
                        print ("last saved time :",duplicate["Last saved"])
                        print("Your file has been opened successfully")
        except FileNotFoundError:
            if not silent:
                print("File not found, Please try again")
            return
        except json.JSONDecodeError:
            if not silent:
                print("Error decoding JSON, Please try again")
            return
    def qr_code(self):
        name=input("Please enter your name to search and provide the details using QR code :")
        if name not in self.name_folder_1:
            print("Your name is not available in our databases")
            return
        details_1=self.name_folder_1[name]
        details_2=details_1["ID"]
        details_3=details_1["Last saved"]
        main_details=(f"Name : {name}\n ID={details_2}\n Last saved={details_3}")
        img=qrcode.make(main_details)
        unique_id=uuid.uuid4().hex
        file=(f"{unique_id}qr.png")
        img.save(file)
        try:
            img.show()
            time.sleep(15.0)
            if os.path.exists(file):
                os.remove(file)
        except Exception as e:
            print(f"Unable to open the image viewer. Please open '{unique_id}_qr.png' manually to view the QR code.")
    def menu(self): #This is the menu part where the options can be accessed
        while True:
            print("^"*15+"MENU for DATABASE MANAGEMENT SYSTEM"+"^"*15)
            print("1-Enter name")
            print("2-Search Name")
            print("3-Save Names")
            print("4-Load Names")
            print("5-Exit")
            print("6-Generate QR Code")
            print("7- Delete")
            print("="*50)
            try:
                choice=int(input("Please enter your choice :"))
            except ValueError:
               print("Invalid input, Please enter a number")
               continue
            if choice==1:
                self.name_enter()
            elif choice==2:
                 self.search_name()    
            elif choice==3:
                self.save_names()
            elif choice==4:
                self.file_load()
            elif choice==5:
                self.save_names()
                print("Thank you for using the program, Your Progress has been saved")
                sys.exit()
            elif choice==6:
                self.qr_code()
            elif choice==7:
                self.del_data()
        print("Invalid choice, Please try again")
        return
manager=NameManager()
manager.file_intro()
manager.menu()