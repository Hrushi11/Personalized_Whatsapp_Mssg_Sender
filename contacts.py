import numpy as np
import pandas as pd
from datetime import datetime

class Extract_contacts:
    def __init__(self, path_to_excel):
        self.df = ""
        self.contacts = 0
        self.contact_name = []
        self.path = path_to_excel
        self.contact_ph_number = []
        self.now_hr = int(str(datetime.now()).split()[1].split(":")[0])
        self.now_min = int(str(datetime.now()).split()[1].split(":")[1]) + 1

    def get_dataframe(self):
        self.df = pd.read_excel(self.path)
        self.df["Contact's Public Display Name \t\t\t"] = self.df["Contact's Public Display Name \t\t\t"].fillna("")
        return self.df

    def get_contact_details(self):
        self.df = self.get_dataframe()
        self.contact_name = np.array(self.df["Contact's Public Display Name \t\t\t"])
        contact_ph_num = np.array(self.df["Phone Number \t\t\t\t\t"])
        self.contacts = len(self.contact_name)

        for i in range(len(contact_ph_num)):
            elem = "+" + str(contact_ph_num[i])
            self.contact_ph_number.append(elem)
        self.contact_ph_number = np.array(self.contact_ph_number)

        return self.contact_name, self.contact_ph_number

if __name__ == "__main__":
    path = "Read/nansns.xlsx"
    contacts = Extract_contacts(path)
    print(contacts.get_contact_details())