import csv
from datetime import datetime
import random
# date_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
# string_date = date_time.strftime("%d/%m/%Y %H:%M:%S")

#!Generates a random date from a range of two dates
def get_datetime():
    date_time = []
    initial = datetime(2017, 1, 30)
    final = datetime(2017, 5, 28) 
    random_date = initial + (final - initial) * random.random()
    random_date = random_date.strftime("%m-%d-%Y %H:%M:%S")
    date_time.append(random_date)
    return date_time


	
#!Generates a random payment type from the list of payment options

payment_type = ["Card", "Internet Banking", "UPI", "Wallet"]
def payment():
    p_type = []
    random_payment = random.SystemRandom()
    pay = random_payment.choice(payment_type)
    p_type.append(pay)
    return p_type

  
#!Generates a random product quantity
def get_quantity():
    qt = []
    qty = (random.random()*20 + 1).__round__()
    qt.append(qty)
    return qt
get_quantity()


#!Generates a random data
def generate_data():
    data_gen =[*get_quantity(),  *payment(), *get_datetime()]
    # print("Generate: 1 ", data_gen )
    return data_gen 


#! Calling generate_data Function x times
def multiple_data():
    data_collection = []
    for _ in range(1000):
        data_collection.append(generate_data())
        # print("M : 222",  data_collection)
    return data_collection

 
 
    
if __name__ == '__main__':
    
#!Generates a CSV file and save it to payment.csv 
    data = multiple_data()
    for d in data:
        # print("loop", d)
    # print("CSV: 3", data)
     with open('payment.csv', 'w', encoding='UTF8') as f:
        csv_writer = csv.writer(f)
        writer = csv.writer(f)
        writer.writerows(data)
        

    