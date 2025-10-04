def get_salary():
    while True:
        try:
            salary = float(input("Enter your total salary: "))
            if salary < 0:
                print("Salary cannot be negative. Try again.")
                continue
            return salary
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_currency():
    while True:
        currency = input("Enter your preferred currency symbol (e.g., ₱, $, €, ¥): ").strip()
        if currency:
            return currency
        else:
            print("Currency cannot be empty. Try again.")

def get_ratios():
    while True:
        try:
            ratios = input("Enter four ratios (percentages) separated by commas (e.g., 40,30,20,10): ")
            ratio_list = [float(r.strip()) for r in ratios.split(",")]
            if len(ratio_list) != 4:
                print("Please enter exactly four values.")
                continue
            total = sum(ratio_list)
            if total != 100:
                print(f"Ratios must sum to 100%. Your total was {total}%. Try again.")
                continue
            return ratio_list
        except ValueError:
            print("Invalid input. Please enter numeric values separated by commas.")

def calculate_allocation(salary, ratios):
    return [salary * (r / 100) for r in ratios]

def print_allocation(allocations, currency):
    print("\nSalary Allocation Breakdown:")
    for i, amount in enumerate(allocations, start=1):
        print(f"  Division {i}: {currency}{amount:,.2f}")

def main():
    currency = get_currency()
    salary = get_salary()
    ratios = get_ratios()
    allocations = calculate_allocation(salary, ratios)
    print_allocation(allocations, currency)

if __name__ == "__main__":
    main()
