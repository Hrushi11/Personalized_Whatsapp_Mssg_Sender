import pywhatkit
from contacts import Extract_contacts

mssgs = []
extractor = Extract_contacts("Read/read.xlsx")
names, ph_numbers = extractor.get_contact_details()

hr = extractor.now_hr
min_ = extractor.now_min

for i in range(extractor.contacts):
    # tag = " @" if names[i] != "" else ""
    tag = "" if names[i] == "" else " "
    mssg = f"Hi{tag}{names[i]},\nThanks a lot for your well wishes on my birthday."
    mssgs.append(mssg)

for i in range(64, extractor.contacts):
    # min_ = 0 if min_ == 60 else min_
    # hr = hr + 1 if min_ == 60 else hr
    pywhatkit.sendwhatmsg(ph_numbers[i], mssgs[i], time_hour=hr, time_min=min_)
    min_ += 1

# To write the messages in a file for test
# with open("birthday-wishes.txt", "w", encoding="utf-8") as f:
#     for i in range(extractor.contacts):
#         f.write(mssgs[i])
#         f.write("\n--------------------------------------")
#         f.write("\n")