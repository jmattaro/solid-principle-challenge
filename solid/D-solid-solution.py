from abc import ABC, abstractmethod
class PaymentType(ABC):
    @abstractmethod
    def payment(self,acount:str,amount:float):
        pass

class PaymentPaypal(PaymentType):
    def payment(self, acount:str, amount:float):
        print("Pago realizado por medio de Paypal")

class PaymentCredirCard(PaymentType):
    def payment(self, acount:str, amount:float):
        print("Pago realizado por medio de Tarejeta de Credito")


class PaymentBitcoins(PaymentType):
    def payment(self, acount:str, amount:float):
        print("Pago realizado por medio de bitcoins")
        
class PaymentProcessor:
    def __init__(self, UseMethod: PaymentType):
        self.MethodPay = UseMethod

    def process_payment(self, acount : str, amount: float):
        self.MethodPay.payment(acount, amount)

def main():
    service = PaymentBitcoins()
    procesar = PaymentProcessor(service)
    procesar.process_payment("55555555555",300)
    
if __name__ == "__main__":
    main()