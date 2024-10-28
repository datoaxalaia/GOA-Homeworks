
name = input("შეიყვანეთ თქვენი სახელი: ")
result = " "

for i in name:
    result += i
    print(i)

num = int(input("შეიყვანეთ რიცხვი: "))

for i in range(num):
    print(i)



result = 0

for i in range(5):
    number = int(input("შეიყვანეთ რიცხვი: "))
    result += number

average = result / 5

print("5 რიცხვის საშუალო არითმეტიკულია: ")

for i in range(-100 , 101 , 2):
    print(i)


while True:

    number = int(input("გთხოვთ, შეიყვანოთ დადებითი რიცხვი: "))
    if number < 0:
        print("თქვენ შეიყვანეთ უარყოფითი რიცხვი. პროგრამა სრულდება.")

    elif number == 0:

        print("ნული არ არის დადებითი რიცხვი. გთხოვთ, სცადოთ ხელახლა.")
    else:
        print("თქვენ შეიყვანეთ დადებითი რიცხვი: ")
