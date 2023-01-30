ticket_number = int(input('Введите номер билета: '))
first_part = (ticket_number // 100000) + (ticket_number // 10000 % 10) + (ticket_number // 1000 % 10)
second_part = (ticket_number // 100 % 10) + (ticket_number // 10 % 10) + (ticket_number % 10)
if first_part == second_part:
   print('Билет счастливый')
else:
   print('Билет несчастливый')