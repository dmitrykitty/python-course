import re
from string import ascii_lowercase


class CardChecker:
    @staticmethod
    def check_card_number(number):
        """Check card number for validity to the format XXXX-XXXX-XXXX-XXXX."""
        format = r"^\d{4}-\d{4}-\d{4}-\d{4}$"
        return bool(re.match(format, number))

    @staticmethod
    def check_card_name(name):
        """Check card name for validity to the format "NAME SURNAME"."""
        format = r"^[A-Za-z]+ [a-zA-z]+$"
        return bool(re.match(format, name))
