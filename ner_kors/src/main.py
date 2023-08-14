from . import schema

file_path = "/Users/ericsmac/Desktop/projects/ner_kors/data/etsy_api/getShopReceipts.json"

## ------------------- Classes -------------------
## NOTE: Initilize with Dependency Injection? 

class transactionObject:
    ## class attributes
    def __init__(self, transaction_id, receipt_id, buyer_email, variations):
        self.transaction_id = transaction_id
        self.receipt_id = receipt_id
        self.buyer_email = buyer_email
        self.variations = variations
    
    ## tranforms personalization detail using kors library and modifies its state
    def variation_transformation(self):
        personalization = self.variations["formatted_value"]
        ## invoke schema

## ------------------- Utility Functions -------------------

## reads and deserializes and returns getShopReceipts endpoint
def get_shop_receipts(file_path):
    with open(file_path, 'r') as file:
        ## returns json object as dict
        data = json.load(file)
        return data
    

## Initializes
def transactionObjectInitializer(get_shop_receipts_dic):
    transactionObjects = {}
    num_of_receipts = get_shop_receipts_dic["count"]
    receipts = get_shop_receipts_dic["results"]
    if (num_of_receipts > 0):
        for receipt in receipts:
            sku = receipt["transactions"]["sku"]
            transaction_id = receipt["transactions"]["transaction_id"]
            buyer_email = receipt["buyer_email"]
            receipt_id = receipt["receipt_id"]
            variations = receipt["transactions"]["variations"]
            transactionObject[sku] = transactionObject(transaction_id, receipt_id, buyer_email, variations)
        return transactionObjects
    return None








# Calls
transactionObjectInitializer(get_shop_receipts(file_path))
