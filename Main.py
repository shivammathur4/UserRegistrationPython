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
        logger.info("Entered first name {}".format(ValidateUser.ValidateName(firstName)))
        
        lastName = input("Enter your Last Name: ")
        logger.info("Entered last name {}".format(ValidateUser.ValidateName(lastName)))

        email = input("Enter your Email: ")
        logger.info("Entered email {}".format(ValidateUser.ValidateEmail(email)))
        
    except Exception as e:
        logger.error(e)
    
    
if __name__ == "__main__":
    getUserInput()
