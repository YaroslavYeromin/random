import random

def get_numbers_ticket(min, max, quantity):
    if min < 0 or max > 1000 or quantity<=0:
       raise ValueError("Некоректный ввод чисел")
    if min > max :
       raise ValueError("минимальное значение не может быть больше максимального")
    if quantity > (max - min) :
        raise ValueError("Колличсетво чисел больше чем в диапазоне")
    return random.sample(range(min , max) , quantity)
        
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)
