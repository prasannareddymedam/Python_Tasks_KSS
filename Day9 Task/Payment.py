""" An online store supports multiple payment methods: CreditCard, UPI, and 
NetBanking. Create a base class Payment with a method process_payment() and 
override it in each payment type.
"""

class Payment:
    def process_payment(self):
        print("Payment Done")

class CreditCard(Payment):
    def process_payment(self):
        print("Paid by CreditCard")

class UPI(Payment):
    def process_payment(self):
        print("Paid by UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Paid by NetBanking")

CreditCard().process_payment()
UPI().process_payment()
NetBanking().process_payment()
