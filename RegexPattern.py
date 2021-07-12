
class RegexPattern:
    NAME_PATTERN = "^[A-Z]{1}[a-z]{2,}"
    EMAIL_PATTERN = "^[a-zA-Z]+(\.[a-z-]+)@?[A-Za-z0-9-]+(\.[a-z]+)*(\.[a-z]{2,})$"
    PHONE_PATTERN = "^[\+][9?][1?][\-\s?][6-9]{1}[\d]{9}$"
