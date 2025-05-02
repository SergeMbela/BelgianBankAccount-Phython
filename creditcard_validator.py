import re

def validate_card(card_number: str) -> str:
    card_number = card_number.replace(" ", "").replace("-", "")  # Remove spaces and dashes

    patterns = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$"
    }

    for card_type, pattern in patterns.items():
        if re.fullmatch(pattern, card_number):
            return f"Valid {card_type} card number."

    return "Invalid card number."

# Examples
print(validate_card("4111 1111 1111 1111"))  # Visa
print(validate_card("5500 0000 0000 0004"))  # MasterCard
print(validate_card("3400 000000 00009"))    # American Express
print(validate_card("6011 0000 0000 0004"))  # Discover
print(validate_card("1234 5678 9012 3456"))  # Invalid
