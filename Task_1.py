number = int(input("Введите  число: "))
third_number = number % 10
second_number = (number // 10) % 10
first_number = number // 100
print(first_number + second_number + third_number)