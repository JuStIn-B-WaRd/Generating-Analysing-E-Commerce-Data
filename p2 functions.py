#Imports
from fileinput import close
import csv
import random

#Global variables
ng_list = []

cities = []

states = []

ecommerce_website_name = [
    "Car Max",
    "AutoTrader",
    "Carvana",
    "Carfax",
    "eBay"
]


#Functons
def website(): #Prints webstite name based on values from generated values in ng_list
    for i in range(len(ng_list)):
        if int(ng_list[i]) == 0:
            print (ecommerce_website_name[0])
        elif int(ng_list[i]) == 1:
            print (ecommerce_website_name[1])
        elif int(ng_list[i]) == 2:
            print (ecommerce_website_name[2])
        elif int(ng_list[i]) == 3:
            print (ecommerce_website_name[3])
        elif int(ng_list[i]) == 4:
            print (ecommerce_website_name[4])
        else:
            print("NULL")

def number_generator(): #Randomly creates user-defined values and stores into ng_list
    i = int(input("# of Datapoints: "))
    n = int(input("# of Variations: "))
    for each in range(i): 
        x = random.randrange(0,n)
        ng_list.append(x)
    return ng_list

def cities_array(): #Builds the cities array from stored csv file
    with open('cities.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            cities.append(line[0])
        #print(cities)

def states_array(): #Builds the states array from stored csv file
    with open('cities.csv', 'r') as csv_file:    
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            states.append(line[1])
        #print(states)

def locations(): #Prints city and state name based on values from generated values in ng_list
    #UGLY AF, BUT WORKS
    for i in range(len(ng_list)):
        if int(ng_list[i]) == 0:
            x = random.randrange(0,4)
            cit_str = str(cities[x])
            st_str = str(states[0])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 1:
            x = random.randrange(4,7)
            cit_str = str(cities[x])
            st_str = str(states[4])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 2:
            x = random.randrange(7,20)
            cit_str = str(cities[x])
            st_str = str(states[7])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 3:
            x = random.randrange(20,26)
            cit_str = str(cities[x])
            st_str = str(states[20])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 4:
            x = random.randrange(26,31)
            cit_str = str(cities[x])
            st_str = str(states[26])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 5:
            x = random.randrange(31,35)
            cit_str = str(cities[x])
            st_str = str(states[31])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 6:
            x = random.randrange(35,38)
            cit_str = str(cities[x])
            st_str = str(states[35])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 7:
            x = random.randrange(38,46)
            cit_str = str(cities[x])
            st_str = str(states[38])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 8:
            x = random.randrange(46,50)
            cit_str = str(cities[x])
            st_str = str(states[46])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 9:
            x = random.randrange(50,58)
            cit_str = str(cities[x])
            st_str = str(states[50])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 10:
            x = random.randrange(58,63)
            cit_str = str(cities[x])
            st_str = str(states[58])
            fin_str = cit_str + "," + st_str
            print(fin_str)
        elif int(ng_list[i]) == 11:
            x = random.randrange(63,67)
            cit_str = str(cities[x])
            st_str = str(states[63])
            fin_str = cit_str + "," + st_str
            print(fin_str)

def main(): #Main method
    cities_array()
    states_array()
    number_generator()
    website()
    number_generator()
    locations()

#Execute Statement
if __name__ == '__main__':
    main()

