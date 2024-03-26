import csv
import random
from datetime import datetime, timedelta

# Function to generate random datetime within a specified range
def random_datetime(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)
    return start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes, seconds=random_seconds)

# Define start and end dates for data generation
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Open a CSV file in write mode
with open('weather_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Date', 'Time', 'Temperature(C)', 'Humidity(%)', 'Rainfall(mm)'])
    
    # Generate 10,000 data points
    for _ in range(10000):
        # Generate random datetime
        random_date = random_datetime(start_date, end_date)
        date_str = random_date.strftime('%Y-%m-%d')
        time_str = random_date.strftime('%H:%M')
        
        # Generate random temperature, humidity, and rainfall values
        temperature = round(random.uniform(15, 35), 2)
        humidity = round(random.uniform(40, 90), 2)
        rainfall = round(random.uniform(0, 10), 2)
        
        # Write data row
        writer.writerow([date_str, time_str, temperature, humidity, rainfall])

print("CSV file generated successfully.")
