def main():
    owed = 50
    while owed > 0:
        print("Amount due:", owed)
        paid = int(input("Insert Coin: "))
        #make it look pretty
        print()
        #only accept specific coins
        if paid == 5 or paid == 10 or paid == 25:
            owed -= paid
    print("Change owed:", abs(owed))


main()