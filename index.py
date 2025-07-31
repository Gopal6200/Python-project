import pandas as pd
from datetime import datetime

# Store weather data and unique dates
weather_data = []
unique_dates = set()

def validate_date(date_str):
    """Validate date in YYYY-MM-DD format"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_weather_entry():
    """Add a new weather entry with validation"""
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format.")
        return
    if date in unique_dates:
        print("Duplicate entry. Date already exists.")
        return
    try:
        temperature = float(input("Enter temperature (°C): "))
    except ValueError:
        print("Invalid temperature.")
        return
    condition = input("Enter weather condition (e.g., Sunny, Rainy): ").capitalize()

    entry = {"Date": date, "Temperature": temperature, "Condition": condition}
    weather_data.append(entry)
    unique_dates.add(date)
    print("Entry added successfully.")

def view_weather_data():
    """Display all recorded weather data"""
    if not weather_data:
        print("No data available.")
        return
    df = pd.DataFrame(weather_data)
    print("\nWeather Data:\n", df)

def summarize_data():
    """Display average temperature"""
    if not weather_data:
        print("No data to summarize.")
        return
    df = pd.DataFrame(weather_data)
    avg_temp = df["Temperature"].mean()
    print(f"\nAverage Temperature: {avg_temp:.2f} °C")

def export_to_csv():
    """Export data to CSV file"""
    if not weather_data:
        print("No data to export.")
        return
    df = pd.DataFrame(weather_data)
    df.to_csv("weather_data.csv", index=False)
    print("Data exported to 'weather_data.csv'.")

def menu():
    """Main menu loop"""
    while True:
        print("\nWeather Data Recorder Menu:")
        print("1. Add Weather Entry")
        print("2. View Weather Data")
        print("3. Summarize Data")
        print("4. Export to CSV")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_weather_entry()
        elif choice == '2':
            view_weather_data()
        elif choice == '3':
            summarize_data()
        elif choice == '4':
            export_to_csv()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
