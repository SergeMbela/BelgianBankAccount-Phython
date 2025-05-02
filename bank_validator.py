# bank_validator.py

class BelgianBankAccountValidator:
    @staticmethod
    def is_valid(bban: str) -> bool:
        clean = bban.replace(" ", "")
        if len(clean) != 12 or not clean.isdigit():
            return False
        base = clean[:10]
        control = int(clean[10:])
        modulo = int(base) % 97
        expected_control = 97 if modulo == 0 else modulo
        return expected_control == control
