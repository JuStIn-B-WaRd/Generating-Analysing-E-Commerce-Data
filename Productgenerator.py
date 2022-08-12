
import random

def main():
    with open("product_file.csv", "w") as f:
        for i in range(5):
            x = random.randint(1, 25)
            print(x)
            if x == 1:
                f.write("100243,F-150,Ford,45525.00\n")
            elif x == 2:
                f.write("100145,Silverado,Chevrolet,34600.00\n")
            elif x == 3:
                f.write("100379,1500,Ram,33975.00\n")
            elif x == 4:
                f.write("200482,RAV4,Toyota,26975.00\n")
            elif x == 5:
                f.write("300479,Camry,Toyota,25945.00\n")
            elif x == 6:
                f.write("200528,Grand Cherokee,Jeep,39000.00\n")
            elif x == 7:
                f.write("100648,Sierra,GMC,37195.00\n")
            elif x == 8:
                f.write("100494,Highlander,Toyota,35855.00\n")
            elif x == 9:
                f.write("300451,Corolla,Toyota,20425.00\n")
            elif x == 10:
                f.write("200122,Equinox,Chevrolet,26300.00\n")
            elif x == 11:
                f.write("200787,CR-V,Honda,26800.00\n")
            elif x == 12:
                f.write("100409,Tacoma,Toyota,27150.00\n")
            elif x == 13:
                f.write("300857,Model Y,Tesla,65990.00\n")
            elif x == 14:
                f.write("200233,Explorer,Ford,35510.00\n")
            elif x == 15:
                f.write("400562,Wrangler,Jeep,30295.00\n")
            elif x == 16:
                f.write("300804,Model 3,Tesla,46990.00\n")
            elif x == 17:
                f.write("200967,Rogue,Nissan,27150.00\n")
            elif x == 18:
                f.write("201081,Tucson,Hyundai,24950.00\n")
            elif x == 19:
                f.write("201137,CX-5,Mazda,26250.00\n")
            elif x == 20:
                f.write("300723,Accord,Honda,26520.00\n")
            elif x == 21:
                f.write("300995,Altima,Nissan,24900.00\n")
            elif x == 22:
                f.write("201278,Outback,Subaru,26945.00\n")
            elif x == 23:
                f.write("200261,Escape,Ford,27185.00\n")
            elif x == 24:
                f.write("200794,HR-V,Honda,23650.00\n")
            elif x == 25:
                f.write("300786,Civic,Honda,22550.00\n")


if __name__ == "__main__":
    main()