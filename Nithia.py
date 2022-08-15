import csv
from faker import Faker
import random

# Status of the payment (Success or Failed)
def payment_status():
    range = random.randint(0, 100)
    if range < 80:
        return True
    else:
        return False

# Failure reasons
def reason(success):
    if success == False:
        reasons = ["The payment gateway does not support", "Merchant account blocks the transaction", "The billing address is invalid ", "Credit or debit card is expired ", "Credit or debit card is canceled", "Incorrect Pin", "The consumers account is suspended or closed "]
        rof = random.choice(reasons)
        return f"{rof}"
    else:
        return "payment success"

# CSV generation
def datagenerate(records, headers):
    fake = Faker('en_US')
    with open("Payment_data.csv", 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):   
            if payment_status() == True:
                status = "Success"
                temporary_value = True
            else:
                status = "Failed"
                temporary_value = False
            reason_for_failure = reason(temporary_value)
              
            writer.writerow({
                    "payment_txn_id" : fake.bothify(text='??-######'),
                    "payment_txn_success" : status,
                    "failure_reason" : reason_for_failure                   
                    })
    
if __name__ == '__main__':
    records = 5500
    headers = ["payment_txn_id", "payment_txn_success", "failure_reason"]
    datagenerate(records, headers)
    print("CSV generation complete!")