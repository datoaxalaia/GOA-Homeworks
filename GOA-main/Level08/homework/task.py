print("-----------N1------------")

age = int(input("შეიყვანეთ თქვენი ასაკი: "))
age1 = age > 13 and age < 19
print(age1)
print("-----------N2------------")

is_A = 10
print(is_A > 9)
print("-------------------------")
is_B = 8 and 10
print(is_B > 8)
print("-------------------------")
is_C = 7 and 8
print(is_C > 7)
print("-------------------------")
is_D = 6 and 7
print(is_D > 5)
print("-------------------------")
is_F = 6
print(is_F > 5)

print("-----------N3------------")

num1 = True or False
print(num1)
num2 = True and False
print(num2)

print("-----------N4------------")
number1 = input("შეიყვანეთ რიცხვი პირველი: ")
number2 = input("შეიყვანეთ რიცხვი მეორე: ")

print(number1 == number2)
print(number1 < number2)
print(number1 > number2)
print(number1 <= number2)
print(number1 >= number2)
print(number1 != number2)

print("-----------N5------------")

a = 40
b = 20
c = 10

is_a_greatest = True or False
is_b_middle = True and True
is_c_least = True or False

print(is_a_greatest,is_b_middle,is_c_least)
print("-----------N6------------")

score = 100

is_pass = True or False
is_high_pass = True and False
is_perfect = True and True
is_failing = False or True

print(is_pass,is_high_pass,is_perfect,is_failing)
print("-----------N7------------")

P = True or False
Q = False and True

P_and_not_Q = True or False
not_P_and_Q = False and True
P_xor_Q = True and True

print(P_and_not_Q,not_P_and_Q,P_xor_Q)




