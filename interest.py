def get_positive_float(prompt):
    """Ensures the user enters a valid positive float."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def get_positive_int(prompt, min_value=0):
    """Ensures the user enters a valid positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                raise ValueError(f"Value must be at least {min_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def compound_interest(P, r, n, t, PMT):
    """Calculates compound interest with monthly contributions."""
    return P * (1 + r/n)**(n*t) + (PMT * (((1 + r/n)**(n*t) - 1) / (r/n)))

def main():
    print("📈 Welcome to the Compound Interest Calculator!\n")

    # Get user inputs
    age = get_positive_int("Enter your current age: ", min_value=0)
    retirement_age = get_positive_int("Enter the age you plan to retire: ", min_value=age+1)
    initial_deposit = get_positive_float("Enter the initial deposit amount: ")
    annual_savings = get_positive_float("Enter the amount you save each year: ")
    annual_interest_rate = get_positive_float("Enter the annual interest rate (in %): ") / 100
    
    # Calculate investment duration
    years = retirement_age - age

    # Monthly values
    n = 12  # Monthly compounding
    PMT = annual_savings / 12  # Monthly savings contribution

    # Compute future value
    final_amount = compound_interest(initial_deposit, annual_interest_rate, n, years, PMT)
    
    # Display results
    print("\n**Results**")
    print(f"Total years invested: {years} years")
    print(f"Total amount saved (without interest): ${annual_savings * years:,.2f}")
    print(f"Final amount after compounding: **${final_amount:,.2f}**\n")

if __name__ == "__main__":
    main()
