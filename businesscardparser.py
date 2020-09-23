# Kelley Li
# 9/22/2020

# imports
import nltk # for natural language processing
import re # for regex expressions
import contactinfo

# Class to parse information from given text
class BusinessCardParser():
    contact_info = None
    def __init__(self):
        pass

    # Uses nltk library to find name in provided array
    # Input: Array from text input
    # Output: A string of all identified as names
    #
    # TODO: Currently assumes that name is all on one line and only on one line
    # There are few business cards where this is not the case, but it's risky
    # I'm not really sure how else to handle this
    def getName(self, sentence_array):
        # variable to return
        name = ""

        for fragment in sentence_array:
            # only allows for name on one line
            if(name == ""):
                # seperates words into tokens
                word_tokens = nltk.word_tokenize(fragment)

                # tags word tokens (parts of speech)
                word_tags = nltk.pos_tag(word_tokens)

                # gets names
                # chunks the fragment
                fragment_chunks = nltk.chunk.ne_chunk(word_tags)
                # print(fragment_chunks) # check how the words are tagged
                for chunk_word in fragment_chunks:
                    # if the chunk is a tree type
                    if(type(chunk_word) == nltk.tree.Tree):
                        # get node label)
                        chunk_word_label = chunk_word.label()
                        # if the word is labeled person OR if the word before it was
                        if(chunk_word_label == 'PERSON' or name != ""):
                            # check if there's a better method for tree traversal
                            name += " ".join(word[0] for word in chunk_word.leaves()) + " "

        if(name == ""):
            return "Error: No name found"
        return name.strip()


    # Uses regex to find phone numbers in a number of formats  
    # Input: Array from text input
    # Output: Returns the first 7 - 11 digit phone number in the text
    #
    # TODO Currently leaves too much room for error in the regex expression
    # Also need to make sure to account for newlines in parsing number
    def getPhoneNumber(self, sentence_array):
        # create a string from the array to search through, could also iterate through
        sentence = " ".join(sentence_array)
        # regex for general number formats
        number = re.search("\d{0,1}[^:]{0,2}\d{0,3}\D{0,2}\d{3}\D{0,1}\d{4}", sentence)
        if(number):
            return re.sub("\D", "", number.group().strip())
        return "Error: No number found"


    # Uses regex to find an email based off the [stuff]@[stuff].[stuff] format
    # Input: Array from text input
    # Output: Returns the first string matching the email format above
    def getEmailAddress(self, sentence_array):
        email = ""
        # Iterates though the sentence array
        for line in sentence_array:
            # searches for string that matches email format
            email = re.search(".+@.+\..+", line)
            # if non empty, return cleaned result
            if(email):
                return email.group().strip()
        return "Error: No email found"


    # Calls the functions to get info from a block of text and create a ContactInfo object
    # Input: document - the text from the business card, seperated by newlines
    # Output: Returns a ContactInfo object initialized with the requisite parameters
    def getContactInfo(self, document):
        sentence_array = document.split("\n")
        contact_info = contactinfo.ContactInfo(self.getName(sentence_array), 
        self.getPhoneNumber(sentence_array), 
        self.getEmailAddress(sentence_array))
        return contact_info