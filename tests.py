# Kelley Li
# 9/22/2020
# This file is for testing the functionalites in main.py

# imports
import unittest
import main
import businesscardparser
import contactinfo

# Use descriptive names

class TestFunctions(unittest.TestCase):
    def setUp(self):    
        self.strings = ['ASYMMETRIK LTD', 'Mike Smith', 'Senior Software Engineer',
         '(410)555-1234', 'msmith@asymmetrik.com']
        self.business_card_parser = businesscardparser.BusinessCardParser()

    def testGetName(self):
        name = self.business_card_parser.getName(self.strings)

        self.assertEqual(name, "Mike Smith")

    def testGetPhoneNumber(self):
        phone_number = self.business_card_parser.getPhoneNumber(self.strings)
        
        self.assertEqual(phone_number, "4105551234")

    def testGetEmailAddress(self):
        email_address = self.business_card_parser.getEmailAddress(self.strings)

        self.assertEqual(email_address, "msmith@asymmetrik.com")

    def testBusinessCardParser(self):
        document = """ASYMMETRIK LTD
Mike Smith
Senior Software Engineer
(410)555-1234
msmith@asymmetrik.com"""
        contact_info = self.business_card_parser.getContactInfo(document)
        answer = contactinfo.ContactInfo("Mike Smith", "4105551234", "msmith@asymmetrik.com")
        self.assertTrue(contact_info.toString() == answer.toString())


if __name__ == "__main__":
    unittest.main()
    print("Passed")