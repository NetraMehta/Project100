class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def cashWithdrawl(self):
        print('*** amount of cash has been withdrawn')

    def balanceEnquiry(self):
        print('your balance is ****')

netra = Atm('0098 2345 8756 2947', '345')

netra.cashWithdrawl()
netra.balanceEnquiry()

print(netra.cardNumber)
print(netra.pinNumber)