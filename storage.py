import os
import json
from logger import log_info
def save_names(record_manager):
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(BASE_DIR,"data.json")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    temp_path=os.path.join(BASE_DIR,"Data.temp")
    data_to_save=record_manager.records
    try:
        record_manager.records_save(file_path,data_to_save,temp_path)
        log_info("Data saved successfully", level="INFO")
    except PermissionError as e:
        print(f" Error :Permission denied, {e}")
        log_info(f"Permission denied on save: {e}", level="ERROR")
        return
    except json.JSONDecodeError as e:
        print(f"Error: failed encoding JSON, {e}")
        log_info(f"JSON encoding error: {e}", level="ERROR")
        return
    except Exception as e:
        print(f"Error: {e}")
        log_info(f"ERROR : {e}", level="CRITICAL")
def file_load(record_manager,silent=False):
    try:
        BASE_DIR=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(BASE_DIR,"data.json")
        print("Data in :",(BASE_DIR))
        print("Trying to open :",os.path.abspath(file_path))
        print("Does the data exists in JSON :",os.path.exists(file_path))
        result = record_manager.load_file(file_path)
        if isinstance(result, dict):
            record_manager.records = result
        log_info("Data loaded successfully", level="INFO")
    except FileNotFoundError as e:
        if not silent:
            print(f"Error: File not found, {e}")
            log_info(f"Data file not found: {e}", level="ERROR")
        return
    except json.JSONDecodeError as e:
        if not silent:
            print(f"Error: failed decoding JSON, {e}")
            log_info(f"JSON decode error on load: {e}", level="ERROR")
        return
    except Exception as e:
        print("An Unknown Error Occured")
        log_info(f"ERROR : {e}",level="CRITICAL")