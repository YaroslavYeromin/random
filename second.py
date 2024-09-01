from datetime import datetime

def get_days_from_today(date) :
    
    
    year = 2023
    mounth = 9
    day = 1
    if mounth > 12 or day > 31 or year < 0:
        return "некоректный ввод"
              
    date = datetime(year , mounth , day ).date()
        
    date_today = datetime.today().date()
  
    delta_date = date_today - date
    
    
    return delta_date.days
days_dif =get_days_from_today("2020.12.12")
print(days_dif)
