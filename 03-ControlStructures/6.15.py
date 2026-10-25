###
# Program checking the validity of an EAN-13 article number
# and verifying if the product was manufactured in Poland.
#

ean_number = input("Enter EAN-13 article number: ").strip()
if len(ean_number) == 13:
    print("Article number is correct")
    if ean_number[0:3] == "590":
        print("Article manufactured in Poland")