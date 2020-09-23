# Kelley Li
# 9/22/2020

# imports
import businesscardparser


# Gets multiline text input from user and returns a strine
# line as an element
# Input: n/a
# Output: String of user input, seperated by new line
def getUserInput():
    input_text = ""
    next_line = input("Add business card info here (Newline will end input):\n")
    input_text += next_line
    # while there is a next line
    while(next_line):
        # add line to the array
        input_text += "\n" + next_line
        # get next line
        next_line = input()
    return input_text

def main():
    business_card_parser = businesscardparser.BusinessCardParser()
    print(business_card_parser.getContactInfo(getUserInput()).toString())

# Calls main
if __name__ == "__main__":
    main()