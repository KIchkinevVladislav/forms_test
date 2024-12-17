import re


def validate_value(value: str) -> str:
    EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    PHONE_REGEX = re.compile(r"^\+7\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}$")
    DATE_REGEX_DMY = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")
    DATE_REGEX_YMD = re.compile(r"^\d{4}-\d{2}-\d{2}$")


    if EMAIL_REGEX.match(value):
        return "email"
    elif PHONE_REGEX.match(value):
        return "phone"
    elif DATE_REGEX_DMY.match(value) or DATE_REGEX_YMD.match(value):
        return "date"
    else:
        return "text"
