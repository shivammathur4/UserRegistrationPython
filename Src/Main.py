"""
@Author: Shivam Mathur
@Date: 2021-07-09 
@Last Modified by: Shivam Mathur
@Title : Program Aim is to validate user entered details using regular expression.
"""

from UserValidation import ValidateUser
from LogHandler import logger


def getUserInput():
    """
    Description:
        This method is used for getting user input frm the user.
        It calls the validate name method of validate user class for validation of name.

    """
    try:
        firstName = input("Enter your FirstName: ")
        logger.info("Entered first name {}".format(
            ValidateUser.ValidateName(firstName)))

        lastName = input("Enter your Last Name: ")
        logger.info("Entered last name {}".format(
            ValidateUser.ValidateName(lastName)))

        email = input("Enter your Email: ")
        logger.info("Entered email {}".format(
            ValidateUser.ValidateEmail(email)))

        phoneNumber = input("Enter your Phone Number: ")
        logger.info("Entered phone number {}".format(
            ValidateUser.ValidatePhoneNumber(phoneNumber)))

        password = input("Enter your Password: ")
        logger.info("Entered password {}".format(
            ValidateUser.ValidatePassword(password)))

        # passing list of email samples for validation.
        email_sample = ['abc@yahoo.com', 'abc-100@yahoo.com', 'abc.100@yahoo.com', 'abc111@abc.com',
                        'abc-100@abc.net', 'abc.100@abc.com.au', 'abc@1.com', 'abc@gmail.com.com', 'abc+100@gmail.com']
        
        # getting email one by one through for loop and passing for validation
        for item in email_sample:
            print(item)
            logger.info("Entered email {}".format(
            ValidateUser.ValidateEmail(item)))

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    getUserInput()
