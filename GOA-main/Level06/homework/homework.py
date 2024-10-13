age = int(input("ჩაწერე შენი დაბადების წელი: ") )
print(age * age)


სიგრძე = int(input("შეიყვანეთ ოთხკუთხედის სიგრძე: "))
სიგანე = int(input("შეიყვანეთ ოთხკუთხედის სიგანე: "))
პერიმეტრი = int(input("შეიყვანეთ ოთხკუთხედის პერიმეტრი: "))

print("ფართობი: ",სიგრძე * სიგანე)
print("პერიმეტრი: ", პერიმეტრი * (სიგანე + სიგრძე))

school = int(input("დაწერე შენი სახლიდან სკოლამდე რამდენი კილომეტრია: "))
meter = school * 1000
centimeter = school * 100000
miles = school * 1000000
print("მეტრი:",meter)
print("სანტიმეტრი:",centimeter)
print("მილი:",miles)

momname = input("შეიყვანეთ თქვენი დედის სახელი: ")
momsurname =  input("შეიყვანეთ თქვენი დედის გვარი: ")

dadname = input("შეიყვანეთ თქვენი მამის სახელი: ")
dadsurname =  input("შეიყვანეთ თქვენი მამის გვარი: ")

color = input("შეიყვანეთ საყვარელი ფერი: ")
car = input("შეიყვანეთ საყვარელი მანქანა: ")
hobby = input("შეიყვანეთ პირველი საყვარელი ჰობი: ")
hobby2 = input("შეიყვანეთ მეორე საყვარელი ჰობი: ")
hobby3 = input("შეიყვანეთ მესამე საყვარელი ჰობი: ")


print("დედის სახელი: ", momname,"დედის გვარი: ", momsurname,"მამის სახელი : ",dadname, "მამის გვარი: ",dadsurname,"საყვარელი ფერი : ",color,"საყვარელი მანქანა: ",car,"საყვარელი პირველი ჰობი: ",hobby,"საყვარელი მეორე ჰობი: ",hobby2,"საყვარელი მესამე ჰობი: ",hobby3)

num1 = int(input("შეიყვანეთ ორნიშნა რიცხვი: "))

first_number = num1 // 3
second_number = num1 % 9


sum_of_numbers = first_number + second_number

print("თქვენი რიცხვის ციფრების ჯამია: ",sum_of_numbers)




