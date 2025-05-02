# bank_account_balance.py

class CompteBancaire:
    def __init__(self, account_number, titulaire):
        self.account_number = account_number
        self.titulaire = titulaire
        self.solde = 0

    def deposer(self, montant):
        self.solde += montant
        print(f"✅ Dépôt de {montant}€. Nouveau solde : {self.solde}€")

    def retirer(self, montant):
        if montant > self.solde:
            print("❌ Fonds insuffisants.")
        else:
            self.solde -= montant
            print(f"✅ Retrait de {montant}€. Nouveau solde : {self.solde}€")

    def afficher_solde(self):
        print(f"💰 Solde actuel : {self.solde}€")

