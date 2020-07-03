import smtplib
import time
import config

# ABOUT
# This script was originally found on reddit and I adapted it to my personal use.
# It has been especially helpful in cases where I have scripts that may take hours to run 
# by using this I can walk away and get a text when it is ready.


# QUICK LINKS
# To fix the disconnection- https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python 
# or https://stackoverflow.com/questions/17759860/python-2-smtpserverdisconnected-connection-unexpectedly-closed
# to look up a carrier https://www.freecarrierlookup.com/
# to enable insecure apps like this one- https://myaccount.google.com/u/1/lesssecureapps?pageId=none&pli=1

GMAIL_USERNAME = getattr(config, 'GMAIL_USERNAME', 'default value if not found')
GMAIL_PASSWORD = getattr(config, 'GMAIL_PASSWORD', 'default value if not found')
GMAIL_ADDRESS = GMAIL_USERNAME + "@gmail.com"
CELL_PHONE_NUMBER = getattr(config, 'CELL_PHONE_NUMBER', 'default value if not found')

carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint': '@pm.sprint.com',
    'cricket': '@mms.cricketwireless.net'
}


def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number1 = CELL_PHONE_NUMBER.format(carriers['att']) #me
    my_email = GMAIL_ADDRESS
    auth = (GMAIL_USERNAME, GMAIL_PASSWORD)


    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    response = server.sendmail( auth[0], [my_email,to_number1], message)
    print(response)


send("Test")
# no text output but I include a screenshot of the text on my phone in the README
