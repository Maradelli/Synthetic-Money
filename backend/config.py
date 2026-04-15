'''
Constants: weights, categories, etc.

The structure of Dataset:
- Transaction_id (UUID / Int32)
- Timestamp (Datetime)
- Customer_id (String) <- repetative
- Amount (Float32)
- Category (Categorical)
- Merchant_name (String)
- Card_type (String) <- Visa, Mastercard, MIR (can be changed only to MIR if user wants)
- Is_fraud (Bool) <- 1 - Fraud, 0 - Normal
___________________________________________________________________
'''


'''
Dictionary of real russian merchants 
'''
MERCHANTS = {

}

class Persona: #Basic class for clients
    def __init__(self, name: str, modifiers: dict):
        self.name = name
        self.modifiers = modifiers

    def adjust_params(self, base_E: float, base_sigma: float):
        '''
        Method of recalculating parameters for each type
        '''
        return 'TODO'
    
'''
There are 5 psychotypes of clients with unique behaviour and weights
'''
class Goblin(Persona):
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
        self.name = 'GoblinTreasurer'
        self.modifiers = modifiers #TODO

class PartyKing(Persona):
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
        self.name = 'PartyKing'
        self.modifiers = modifiers #TODO


class SonOfMF(Persona):
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
        self.name = 'SonOfMF'
        self.modifiers = modifiers #TODO


class Player(Persona):
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
        self.name = 'UnstoppablePlayer'
        self.modifiers = modifiers #TODO


class Survivalist(Persona):
    def __init__(self, name, modifiers):
        super().__init__(name, modifiers)
        self.name = 'HypSurvivalist'
        self.modifiers = modifiers #TODO
