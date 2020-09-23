# Kelley Li
# 9/22/2020

# Class containing a person's contact info
# Contains getName, getPhoneNumber, and getEmailAddress
class ContactInfo:
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    # returns name
    def getName(self):
        return self.name
    
    # returns phone number
    def getPhoneNumber(self):
        return self.phone_number

    # returns email address
    def getEmailAddress(self):
        return self.email_address

    def toString(self):
        return "Name: " + self.name + "\nPhone: " + self.phone_number + "\nEmail: " + self.email_address


