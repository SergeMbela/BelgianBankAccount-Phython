def identifier_banque_belge(iban):
    banques = {
        "001": "Banque Nationale de Belgique",
        "063": "CBC Banque",
        "068": "Belfius",
        "091": "ING Belgique",
        "132": "Beobank",
        "310": "AXA Banque",
        "751": "Keytrade Bank",
        "829": "Hello Bank",
        # Ajoute d'autres codes si besoin
    }

    iban = iban.replace(" ", "").upper()

    if not iban.startswith("BE") or len(iban) != 16:
        return "IBAN belge non valide"

    code_banque = iban[4:7]
    return banques.get(code_banque, f"Banque inconnue (code : {code_banque})")

# Exemple
iban = "BE68 0630 1234 5678"
print(identifier_banque_belge(iban))