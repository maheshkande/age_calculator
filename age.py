from datetime import datetime

def calculate_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%d-%m-%Y")
        today = datetime.today()

        # Calculate difference
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        # Adjust for negative days/months
        if days < 0:
            months -= 1
            days += 30  # approx correction

        if months < 0:
            years -= 1
            months += 12

        print(f"\n🧮 You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("❌ Please enter date in DD-MM-YYYY format.")

# --- Run App ---
print("📅 Age Calculator")
dob_input = input("Enter your Date of Birth (DD-MM-YYYY): ")
calculate_age(dob_input)
