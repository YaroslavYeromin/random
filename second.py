from datetime import datetime

def days_difference(date):
   
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return ("Некореткный ввод")
        
    current_date = datetime.today().date()
    
    
    difference = current_date - input_date
    
  
    return difference.days



date = "2020-10-32"

print(days_difference(date))
