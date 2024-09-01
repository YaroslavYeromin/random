import random

def get_numbers_ticket(min, max, quantity):
    if min < 0 or max > 1000 or quantity<=0:
        
        return []
        
    if min > max :
        
        return []
    if quantity > (max - min) :
        
        return []
    
    num = random.sample(range(min , max) , quantity)
    sorted_num = sorted(num)
    return sorted_num
        
lottery_numbers = get_numbers_ticket(1,22, 6)
print(lottery_numbers)
