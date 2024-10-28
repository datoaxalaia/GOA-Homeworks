my_list = [1, 2, 3, 4, 5]

my_list[0] = input("შეიყვანეთ პირველი რიცხვი: ")
my_list[1] = input("შეიყვანეთ მეორე რიცხვი: ")
my_list[2] = input("შეიყვანეთ მესამე რიცხვი: ")
my_list[3] = input("შეიყვანეთ მეოთხე რიცხვი: ")
my_list[4] = input("შეიყვანეთ მეხუთე რიცხვი: ")

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])


numbers = [9, 5, 94, 711, 52, 96, 71, 8]


min_number = numbers[0]


for number in numbers:

    if number < min_number:

        min_number = number


print("სიაში ყველაზე პატარა რიცხვია:", min_number)



numbers = [9, 5, 94, 711, 52, 96, 71, 8]


random_item = numbers[3]
print("ჩვენი არჩეული რიცხვია:", random_item)

for number in numbers:
    if number < random_item:
        print("რიცხვი",number, "არის", random_item,"-ზე პატარა")
    else:
        print("რიცხვი", number ,"არ არის", random_item," ზე პატარა")