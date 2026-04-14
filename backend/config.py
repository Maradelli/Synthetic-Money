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
'''

