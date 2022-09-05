from email import message
from tkinter.tix import Tree
import pywhatkit
import pandas as pd
import arguing
# import os # To hide the sender's number

# excel cols to access
require_cols = [3,4,6,7,8]
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('dummy.xlsx', sheet_name=1, usecols=require_cols, header=1)



# Send a message immediately
def send_message_immediately():
    whats_app_number = input("Enter recipient's number: ")
    # whats_app_number = os.getenv('MOBILE') # To hide the sender's number
    message = input("Enter your message: ")

    pywhatkit.sendwhatmsg_instantly(
        phone_no=whats_app_number,
        message=message,
        wait_time=20,
        tab_close=True,
        close_time=3,
    )


# Sending a message at a certain time
def send_message_at_certain_time():
    whats_app_number = input("Enter recipient's number: ")
    # whats_app_number = os.getenv('MOBILE') # To hide the sender's number
    message = input("Enter your message: ")
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))

    pywhatkit.sendwhatmsg(
        phone_no=whats_app_number,
        message=message,
        time_hour=hours,
        time_min=minutes
    )

#sending few message and close the tab
def send_few_message_and_closeTab(number,message):
    send_time = 5
    close_tab = True
    closeTabTime = 10

    pywhatkit.sendwhatmsg_instantly(
        phone_no=number,
        message=message,
        wait_time=send_time,
        tab_close=close_tab,
        close_time=closeTabTime
    )

# Choose which function you want to use
def main():
    excel = arguing.set('--excel', mandatory=True, help_message='excel file data source')
    phoneNumber = arguing.set('--phoneNumberHeader', mandatory=True, help_message='Name of header for phone number colum')
    message = arguing.set('--messageHeader',mandatory=True, help_message='Header name of colom message to send')
    send_message_immediately()
    #send_message_at_certain_time()
    #send_few_message_and_closeTab()


if __name__ == "__main__":
    main()
