"""
@Author: Shivam Mathur
@Date: 2021-07-09
@Last Modified by: Shivam Mathur
@Title : Program Aim is to validate user entered details using regular expression.
"""
import re
from RegexPattern import RegexPattern as regex_pattern
from LogHandler import logger

class ValidateUser:
    
    def ValidateName(input):
        """
    Description:
        This method is used for validating name with regex pattern.

    Return:
        It return a valid true if name is valid and false if it's invalid.
    
    Parameter:
        It takes input as a parameter.
       
    """
        try:
            if (re.match(re.compile(regex_pattern.NAME_PATTERN),input)):
                return "is valid"
            else:
                return "is not valid"
        
        except Exception as e:
            logger.error(e)
        