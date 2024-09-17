print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

seq_num = int(input('Введите количество чисел: '))
max_num = 0
max_sum = 0

for num in range(seq_num):
  user_num = int(input(f'Введите {num + 1}-е число: '))
  digit_sum = 0
  temp_num = user_num
  while temp_num > 0:
    digit_sum += temp_num % 10
    temp_num //= 10
  if digit_sum > max_sum:
    max_sum = digit_sum
    max_num = user_num
print(f'Наибольшая сумма цифр: {max_sum} у числа {max_num}')