'''
Constants: weights, categories, etc.

Classes and OOP.

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
import uuid #for generating unique ids for clients
import math #for calculating parameters of distribution


'''
Dictionary of real russian merchants 
'''
MERCHANTS = {

}

class Persona: #Basic class for clients
    def __init__(self, name: str, modifiers: dict, id: str):
        self.name = name
        self.modifiers = {cat : {'phi' : 1.0, 'alpha' : 1.0} for cat in modifiers.keys()} 
        self.id  = id

    def get_params(self, category : str) -> dict:
        '''
        Method of calculating parameters for each category of transaction for each psychotype of client. 
        It takes into account the base parameters of the category and the modifiers of the client.
        '''
        base = Categories[category]
        mu_base = base[2]
        sigma = base[3]    

        alpha = self.modifiers[category]['alpha']
        mu_final = mu_base + math.log(alpha)
        freq_final = base[0] * self.modifiers[category]['phi']

        return {
            'mu': mu_final,
            'sigma': sigma,
            'frequency_weight': freq_final,
            'min': base[5],
            'max': base[4]
        }
'''
There are 5 psychotypes of clients with unique behaviour and weights
'''
class Goblin(Persona):
    def __init__(self, id: str):
        modifiers = {
            'Food': {'alpha': 0.8, 'phi': 1.3},
            'Dining': {'alpha': 0.5, 'phi': 0.1},
            'Transport': {'alpha': 0.7, 'phi': 1.2},
            'Entertainment': {'alpha': 0.4, 'phi': 0.2}
        }
        super().__init__('GoblinTreasurer', modifiers, id)

class PartyKing(Persona):
    def __init__(self, id: str):
        modifiers = {
            'Dining': {'alpha': 1.5, 'phi': 2.5},
            'Entertainment': {'alpha': 1.8, 'phi': 3.0},
            'Transport': {'alpha': 1.5, 'phi': 1.5}, #Frequent taxis
            'Food': {'alpha': 1.2, 'phi': 0.7} #Rarely cooks
        }
        super().__init__('PartyKing', modifiers, id)

class SonOfMF(Persona):
    def __init__(self, id: str):
        #The benchmark persona - almost no changes to base stats
        modifiers = {} 
        super().__init__('SonOfMF', modifiers, id)

class Player(Persona):
    def __init__(self, id: str):
        modifiers = {
            'Entertainment': {'alpha': 2.0, 'phi': 4.0},
            'Other': {'alpha': 2.5, 'phi': 2.0},
            'Dining': {'alpha': 1.7, 'phi': 1.5}
        }
        super().__init__('UnstoppablePlayer', modifiers, id)

class Survivalist(Persona):
    def __init__(self, id: str):
        modifiers = {
            'Healthcare': {'alpha': 1.4, 'phi': 2.5},
            'Housing and communal services': {'alpha': 1.0, 'phi': 1.1},
            'Food': {'alpha': 0.9, 'phi': 1.1}, # Stocking up
            'Entertainment': {'alpha': 0.5, 'phi': 0.3}
        }
        super().__init__('HypSurvivalist', modifiers, id)

'''
Basic categories of transactions.
The structure of the dictionary is the following:
Category : [distribution in percentage, mean amount, mu, sigma amount, maximum, minimum]
'''
Categories = {
    'Food': [30, 809, 6.685, 0.147, 852, 780],
    'Auto': [10, 15_000, 9.544, 0.379, 97_000, 10_000],
    'Transport' : [5, 316, 5.4, 0.846, 19_376, 121],
    'Housing and communal services': [10, 6800, 8.812, 0.163, 10_651, 4000],
    'Communications': [3, 1100, 6.842, 0.567, 3000, 100],
    'Healthcare': [7, 1293, 7.084, 0.402, 8820, 792],
    'Clothing and shoes': [8, 7196, 8.881, 0.039, 8504, 6738],
    'Restaurants and cafes': [6, 1300, 6.999, 0.584, 5000, 150],
    'Entertainment': [4, 3000, 7.835, 0.584, 10_000, 300],
    'Other': [17, 1500, 6.814, 0.999, 20_000, 50]
}

'''
Time modifiers depending on the time of the day. The structure of the dictionary is the following:
Time of the day : modifier (from 0.0 to 1.0)
'''
Time_modifiers = {
    (0,6): 0.1,
    (6,11): 0.7,
    (11,15): 0.8,
    (15,18): 0.4,
    (18,22): 1.0,
    (22,24): 0.2
    }
