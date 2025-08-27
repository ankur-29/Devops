from datetime import datetime

# Current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Formatting the datetime
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date & Time:", formatted)

# Getting only parts of the date/time
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Creating a custom datetime
custom_date = datetime(2025, 12, 31, 23, 59, 59)
print("Custom Date:", custom_date)