name = "Two Tower"
result = ""

for i in name:
    result += i
    print(i)

print(result)

ricxvi = int(input("შეიყვანეთ რიცხვი: "))
if ricxvi % 2 == 1:
    print("კენტი რიცხვი")
else:
    print("ლუწი რიცხვი")


for ricxvi in range(1, 100):
    if ricxvi % 2 == 0:
        print("ლუწი რიცხვი")
    else:
        print("კენტი რიცხვი")

    
