import pywhatkit

# import os # To hide the sender's number


# Send a message immediately
def send_message_immediately():
    whats_app_number = input("Enter recipient's number: ")
    # whats_app_number = os.getenv('MOBILE') # To hide the sender's number
    message = input("Enter your message: ")

    pywhatkit.sendwhatmsg_instantly(
        phone_no=whats_app_number,
        message=message
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


# Choose which function you want to use
def main():
    send_message_immediately()
    send_message_at_certain_time()


if __name__ == "__main__":
    main()
