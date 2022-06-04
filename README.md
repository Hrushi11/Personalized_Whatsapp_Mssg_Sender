# Personalized Whatsapp Message Sender

Send personalized whatsapp messages to a list of people in a single click with this automation bot. This script uses selenium and beuatiful soup behind the scenes.
Scrape or some how get the contacts in an excel sheet, add that file in the `Read` directory available in the root. Next change the `mssg` variable as per the message
you want to send.

Uncomment the last few lines in `Call.py` to check how the messages will look once they are sent. *Check here: [birthday-wishes.txt](https://github.com/Hrushi11/Personalized_Whatsapp_Mssg_Sender/blob/main/birthday-wishes.txt)* 
The script automatically detects the time and starts exectuting 1 
minute after the execution is started. Once the excecution is started sit back and relax till the messages are sent to all the contacts. The perfect extraction of all 
the contact's phone number and name happens in `contact.py`.

`Extract_contacts` class extracts all the contact's phone number and name and returns it as an array.

![IMG](https://github.com/Hrushi11/Personalized_Whatsapp_Mssg_Sender/blob/main/assets/code.png?raw=true)
