# burger = [0]
# print("Welcome in our fas food")
# toopings =["tomats",'chees','cucumber','meat','bekon','soys']
# for i in range(len(toopings)):
#     print(f"{i + 1}: {toopings[i]}")
#     user = int(input("write your number, which you want plause"))
# while True:
#     if 0 <  user < 9:
#         print("end")
#         break
#     else:
#         burger.append(user)
# print()
import random
burger = []
print("how baker are you wanting")
baker =["кунжутнцю","обычную","без глютена"]
user = int(input("write your number, which you want plause"))
for i  in range(len(baker)):
    print(f"{i + 1}: {baker[i]}")
    if   user not in range(1,3):
        print()
        print("end")
        break
    else:
        burger.append(user)
boom = input("do you want a potato free?Yes/No")
if boom == "Yes":
    print("OK")
else: boom != "Yes"
print("okay")
print("ващ заказ будет готов в течении 15 минут")

random_number = random.randint(0, 100)
print("Your ticket:")
print(random_number)
random_number = random.randint(0, 5000)
print("pricetag zakaza:")
print(random_number)
print("спасибо за покупку")


