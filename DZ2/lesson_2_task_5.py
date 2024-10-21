def month_to_season(month_number):
    if 12 == month_number:
        return "Это Зима!!! Мороз и солнце, день чудесный!!!"
    elif 1 <= month_number <= 2:
        return "Это тоже зима!!!"
    elif 3 <= month_number <= 5:
        return "Это весна!!!!"
    elif 6 <= month_number <= 8:
        return "Это ЛЕТО!!! Солнышком согрето!"
    elif 9 <= month_number <= 11:
        return "Это ОСЕНЬ!!! Унылая пора!"
    else: 
        return "АЙ! ОЙ!  Неверный номер месяца!!!" 
try: 

    month_number = int(input("Введите пожалуйста число месяца от одного до двенадцати:"))
    print (month_to_season(month_number))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")



