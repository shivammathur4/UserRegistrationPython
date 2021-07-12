"""
@Author: Shivam Mathur
@Date: 2021-07-09 
@Last Modified by: Shivam Mathur
@Title : Test case for user registration problem.
"""

from UserValidation import ValidateUser as validate
import unittest


class TestUserValidation(unittest.TestCase):

    #   " Test Case For First Name And LastName "

    def test_givenValidName_shouldReturnTrue(self):
        """
    Description:
        The given valid name should return true in test case

    Parameter:
        It takes self as a parameter.

    """

        self.assertTrue(validate.ValidateName("Shubham"))
        self.assertTrue(validate.ValidateName("Shubh"))

    def test_givenInvalidName_shouldReturnFalse(self):
        """
    Description:
        The given invalid name should return false in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertFalse(validate.ValidateName("Sh"))
        self.assertFalse(validate.ValidateName("shubham"))
        self.assertFalse(validate.ValidateName("SHUBHAM"))
        

     #   " Test Case For Email "

    def test_givenValidEmail_shouldReturnTrue(self):
        """
    Description:
        The given valid email should return true in test case

    Parameter:
        It takes self as a parameter.

    """

        self.assertTrue(validate.ValidateEmail("abc10@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc-100@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc.100@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc111@abc.com"))
        self.assertTrue(validate.ValidateEmail("abc-100@abc.net"))
        self.assertTrue(validate.ValidateEmail("abc.100@abc.com.au"))
        self.assertTrue(validate.ValidateEmail("abc@1.com"))
        self.assertTrue(validate.ValidateEmail("abc@gmail.com.com"))

    def test_givenInvalidEmail_shouldReturnFalse(self):
        """
    Description:
        The given invalid Email should return false in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertFalse(validate.ValidateEmail("shubham@.com"))
        self.assertFalse(validate.ValidateEmail("shivam@gmail"))
        self.assertFalse(validate.ValidateEmail("abc..28@gmail.com"))
        self.assertFalse(validate.ValidateEmail("abc123@gmail.c"))
        self.assertFalse(validate.ValidateEmail("abc@abc@gmail.com"))
        self.assertFalse(validate.ValidateEmail(".abc@abc@gmail.com"))

    
    #   " Test Case For Phone Number "

    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
    Description:
        The given valid Phone number should return true in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertTrue(validate.ValidatePhoneNumber("+91-8120209866"))
        self.assertTrue(validate.ValidatePhoneNumber("+91 8349232195"))

    
    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
    Description:
        The given invalid phone number should return true in test case

    Parameter:
        It takes self as a parameter.

    """
        self.assertFalse(validate.ValidatePhoneNumber("+91-786543"))
        self.assertFalse(validate.ValidatePhoneNumber("+91-78654346578"))
       

     #   " Test Case For Password:  "

    def test_givenValidPassword_shouldReturnTrue(self):
        """
    Description:
        The given valid Password should return true in test case

    Parameter:
        It takes self as a parameter.

    """

        self.assertTrue(validate.ValidatePassword("Shar@789"))
        self.assertTrue(validate.ValidatePassword("jars@Abc98#"))

    def test_givenInvalidPassword_shouldReturnFalse(self):
        """
    Description:
        The given invalid Password should return false in test case

    Parameter:
        It takes self as a parameter.

    """

        self.assertFalse(validate.ValidatePassword("shar@78"))
        self.assertFalse(validate.ValidatePassword("mathur76#"))
        self.assertFalse(validate.ValidatePassword("Shub45eh"))
        
    
