# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

lst = [12,'sadf',5643, 'cdf', 'flk', 8758, 234, 'ddr&&']     
lst_digit = list(filter(lambda x: str(x).isdigit() == True, lst))  # Функция filter  каждый элемент состоящий тоько из цифр в соответстьвующий список 
lst_alpha = list(filter(lambda x: str(x).isalpha() == True, lst))  # Функция filter  каждый элемент состоящий тоько из букв в соответстьвующий список
print(f'Исходный список: {lst}')
print(f'Cписок цифр: {lst_digit}')
print(f'Список букв: {lst_alpha}')
# Элементы содержащие символы выводится не будут 