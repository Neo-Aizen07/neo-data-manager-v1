import os
import json
from logger import log_info
class RecordManager():
    def __init__(self):
        from storage import file_load
        self.records = {}
        file_load(self, silent=True) 
    def update_record(self,username,name,uid,time):
        self.records[username]={
            "Name" : name,
            "ID" : uid,
            "Last Saved" : time
        }
        from storage import save_names as external_save
        external_save(self)
        log_info(f"New record added: {username}", level="INFO")
    def records_save(self,file_path,data_to_save,temp_path):
        if os.path.exists(file_path):
            print("The data is stored locally on ", os.path.abspath(__file__))
            with open(temp_path,"w",encoding="utf-8") as f:
                json.dump(data_to_save,f, indent=4, ensure_ascii=False)
            os.replace(temp_path, file_path)
            print("Data stored successfully")
            return self.records
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4, ensure_ascii=False)
        if os.path.exists(temp_path) and os.path.exists(file_path):
            os.replace(temp_path, file_path)
        print("Data stored successfully")
        return self.records
    def load_file(self,file_path,silent=True):
        try:
            if os.path.exists(file_path):
                with open(file_path,"r") as f:
                    records_dict=json.load(f)
                    return records_dict
        except Exception as e:
            print(f"Load Error: {e}")
            log_info(f"ERROR : {e}", level="ERROR")
            return {}
    def delete_0(self):
        self.records.clear()
        from storage import save_names as delete_save
        delete_save(self)
    def delete_1(self,username):
        if username in self.records:
            del self.records[username]
        else:
            print("Username not found,Please Try Again")
            log_info(f"Delete failed, username not found: {username}", level="WARNING")
        from storage import save_names as delete_user
        delete_user(self)
    def display_data(self):
        return self.records
    def display_user(self,username):
            data=self.records[username]
            if username in self.records:
                print(f"Username : {username}\n Name : {data.get("Name")}\n ID : {data.get("ID")}\n Last Saved : {data.get("Last Saved")}")
                log_info(f"Record displayed: {username}", level="WARNING")
    def delete_person(self):
        from operations import delete_person
        delete_person(self)
    def delete_data(self):
        from operations import delete_data
        delete_data(self)
    def search_func(self):
        from search import search_func
        search_func(self)
    def file_load(self):
        from storage import file_load
        return file_load(self)
    def save_names(self):
        from storage import save_names as external_file
        external_file(self)
    def name_enter(self):
        from user_entry import name_enter as saving_entry
        saving_entry(self)