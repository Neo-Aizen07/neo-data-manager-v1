import os
import datetime
import logging
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
LOG_PATH=os.path.join(BASE_DIR,"error.log")
logging.basicConfig(filename=LOG_PATH,level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s",datefmt="%Y-%m-%d %H:%M:%S")
logger=logging.getLogger(__name__)
def log_info(message,level="INFO"):
    if level=="WARNING":
        logger.warning(message)
    elif level=="INFO":
        logger.info(message)
    elif level=="CRITICAL":
        logger.critical(message)
    elif level=="ERROR":
        logger.error(message)
def log_his(filter_type="all"):
    today=datetime.datetime.today().isoformat(timespec="seconds")
    if not os.path.exists(LOG_PATH):
        print("No log files found")
        return
    with open("error.log","r",encoding="utf-8") as g:
        lines=g.readlines()
        if filter_type=="errors":
            result=[l for l in lines if "ERROR" in l or "CRITICAL" in l]
        elif filter_type=="today":
            result=[l for l in lines if today in l]
        else:
            result=lines
        if not result:
            print("No log record found")
            return
        for lines in result:
            print(lines.strip())
def log_menu():
    while True:
        try:
            print("-"*25+"LOG MENU"+"-"*25)
            print("1. Today's Log")
            print("2. View Error log")
            print("3. Return to  Main Menu")
            choice=int(input("Please enter your choice in integers").strip())
            log_info(f"User Entered the value {choice}",level="INFO")
            if choice==1:
                log_his("today")
            elif choice==2:
                log_his("errors")
            elif choice==3:
                return
        except ValueError:
            log_info("User Entered an Invalid Input",level="WARNING")
        except Exception as e:
            log_info(f"ERROR : {e}",level="CRITICAL")
            print("An Unknown Error Occured")