print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

levels = int(input('Введите высоту пирамиды: '))
current_num = 1
for level in range(1, levels + 1):
  for row in range(levels - level):
    print('  ', end = '')
  for col in range(level):
    print(f'{current_num:2d}', end = '  ')
    current_num += 2  
  print()