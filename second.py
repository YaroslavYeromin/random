from datetime import datetime
date_today = datetime.today().date()
user_date = datetime.strptime("2025.08.20" , "%Y.%m.%d").date()

def get_days_from_today(date) :
    
    date = date_today - user_date
    return date.days
days_dif =get_days_from_today(user_date)
print(days_dif)