from datetime import datetime
 
birthdate = datetime(1990, 3, 13)
 
current_date = datetime.now()
 
days_alive = (current_date - birthdate).days
 
print(f"You have been alive for {days_alive} days.")

