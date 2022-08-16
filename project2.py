import random


def add_customer():
    with open("customer_file.csv", "w") as f:
        for i in range(1, 100):
            x = random.randint(1, 25)
            print(x)
            if x == 1:
                f.write("{}, 1, John Smith\n".format(i))
            elif x == 2:
                f.write("{}, 2, Mary Jane\n".format(i))
            elif x == 3:
                f.write("{}, 3 ,Alexander Hopkins\n".format(i))
            elif x == 4:
                f.write("{}, 4, Rashid Matthews\n".format(i))
            elif x == 5:
                f.write("{}, 5, Brandon Johnson\n".format(i))
            elif x == 6:
                f.write("{}, 6, Alex Poppins\n".format(i))
            elif x == 7:
                f.write("{}, 7, Calvin Harris\n".format(i))
            elif x == 8:
                f.write("{}, 8, Justin Thomas\n".format(i))
            elif x == 9:
                f.write("{}, 9, Chloe Howells\n".format(i))
            elif x == 10:
                f.write("{}, 10, Max Halloway\n".format(i))
            elif x == 11:
                f.write("{}, 11, Chris Jones\n".format(i))
            elif x == 12:
                f.write("{}, 12, Eric Kemsley\n".format(i))
            elif x == 13:
                f.write("{}, 13, James Rodriguez\n".format(i))
            elif x == 14:
                f.write("{}, 14, Kumar Singh\n".format(i))
            elif x == 15:
                f.write("{}, 15, Micheal Smith\n".format(i))
            elif x == 16:
                f.write("{}, 16, Dave Hernandez\n".format(i))
            elif x == 17:
                f.write("{}, 17, Maria Garcia\n".format(i))
            elif x == 18:
                f.write("{}, 18, Susan Boyle\n".format(i))
            elif x == 19:
                f.write("{}, 19, Jordan Brown\n".format(i))
            elif x == 20:
                f.write("{}, 20, Ryan Collier\n".format(i))
            elif x == 21:
                f.write("{}, 21, Louis Way\n".format(i))
            elif x == 22:
                f.write("{}, 22, Jenny Pickard\n".format(i))
            elif x == 23:
                f.write("{}, 23, Usamah Khan\n".format(i))
            elif x == 24:
                f.write("{}, 24, Amy Barnes\n".format(i))
            elif x == 25:
                f.write("{}, 25, Karen Smith\n".format(i))
            else:
                pass


add_customer()
