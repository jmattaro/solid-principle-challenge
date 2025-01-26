from abc import ABC, abstractmethod

class IPaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass
    
class CardGiftLight(IPaymentGateway):
        def pay(self, amount: float) -> None:
            print(f"Gift card Light used to pay {amount}.")
            
        def refund(self, amount: float) -> None:
            raise NotImplementedError("Gift cards Light do not support refunds.")
        
        def handle_dispute(self, dispute_id: str):
             raise NotImplementedError("Gift cards Light do not support disputes.")

class CardGiftGolden(IPaymentGateway):
        def pay(self, amount: float) -> None:
            print(f"Gift card Golden( used to pay {amount}.")
            
        def refund(self, amount: float) -> None:
            raise NotImplementedError("Gift cards Golden do not support refunds.")
        
        def handle_dispute(self, dispute_id: str):
             raise NotImplementedError("Gift cards Golden do not support disputes.")
            
class CardGiftPlatinum(IPaymentGateway):
        def pay(self, amount: float) -> None:
            print(f"Gift card Platinum( used to pay {amount}.")
            
        def refund(self, amount: float) -> None:
            raise NotImplementedError("Gift cards Platinum do not support refunds.")
        
        def handle_dispute(self, dispute_id: str):
             raise NotImplementedError("Gift cards Platinum do not support disputes.")    
    
class AddGiftCard:
    def __init__(self, GardGift :IPaymentGateway ):
        self.Card = GardGift
        
    def Payment(self, amount: float):
        self.Card.pay(amount)
        
    def Refound(self, amount: float):
        self.Card.pay(amount)    
    
    def Dispute(self, amount: float):
        self.Card.pay(amount)   
        
def main():
    giftCard = CardGiftLight()
    Card = AddGiftCard(giftCard)
    Card.Payment(100.0)
    
if __name__ == "__main__":
    main()