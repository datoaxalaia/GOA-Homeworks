i = 1
while i < 2:
    print("goa", i)
    i = 1 + i

for i in range(50):
    print("goa")

num1 = 4
num = 10
for i in range(num1):
    print(num1)
for i in range(num):
    print(num)

pincode = input("შეიყვანეთ პინკოდი: ")
pin = "0800"

while pincode != pin:
    pincode = input("გაიმეორეთ პინკოდი: ")

cashout = input("შეიყვანეთ რამდენი გნებავთ რომ გამოიტანოთ: ")
cash = "1000"
while cashout != cash:
    cashout = input("ამდენ თანხას ვერ გამოიტანთ: ")
print("თქვენ წარმათებით გამოიტანეთ თანხა")

