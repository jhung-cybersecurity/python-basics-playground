amount = float(input("Enter expense amount: "))

if amount > 100:
    print("That is a large expense.")
elif amount > 50:
    print("That is a medium expense.")
elif amount <=0:
    print("The amount is nada.")
else:
    print("That is a small expense.")
