import smtplib
import time
import config

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
    to_number1 = CELL_PHONE_NUMBER.format(carriers['att']) #me
    my_email = GMAIL_ADDRESS
    auth = (GMAIL_USERNAME, GMAIL_PASSWORD)


    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    response = server.sendmail( auth[0], [my_email,to_number1], message)
    print(response)


send("Test")
