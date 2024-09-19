number = input("Введите двузначное число: ")

if len(number) != 2:
    print("Это не двузначное число.")
else:
    if number[0] == number[1]:
        print("Да")
    else:
       print("Нет")