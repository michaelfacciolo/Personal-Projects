import sys
import time
import logging
from typing import Union

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_positive_float(prompt: str) -> float:
    """Ensures the user enters a valid positive float."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                raise ValueError("Value must be greater than zero.")
            return value
        except ValueError as e:
            print(f"❌ Invalid input: {e}. Please enter a valid number.")

def get_positive_int(prompt: str, min_value: int = 1) -> int:
    """Ensures the user enters a valid positive integer above a minimum value."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value < min_value:
                raise ValueError(f"Value must be at least {min_value}.")
            return value
        except ValueError as e:
            print(f"❌ Invalid input: {e}. Please enter a valid whole number.")

def compound_interest(principal: float, rate: float, periods: int, years: int, contribution: float) -> float:
    """Calculates compound interest with periodic contributions."""
    try:
        # Ensures valid interest rate
        if rate < 0 or periods <= 0:
            raise ValueError("Interest rate and periods must be positive values.")
        
        return principal * (1 + rate/periods)**(periods * years) + \
               (contribution * (((1 + rate/periods)**(periods * years) - 1) / (rate/periods)))
    
    except ZeroDivisionError:
        logging.error("❌ Division by zero error in compound interest calculation.")
        sys.exit("Exiting due to calculation error.")

def display_results(years: int, total_saved: float, final_amount: float) -> None:
    """Displays the calculated investment details in a formatted manner."""
    print("\n🔹 **Investment Summary** 🔹")
    print(f"🕒 **Total years invested:** {years} years")
    print(f"💰 **Total amount saved (without interest):** ${total_saved:,.2f}")
    print(f"📈 **Final amount after compounding:** **${final_amount:,.2f}**\n")

def main() -> None:
    print("📊 Welcome to the Compound Interest Calculator!\n")

    # Get user inputs with error handling
    age = get_positive_int("Enter your current age: ", min_value=0)
    retirement_age = get_positive_int("Enter the age you plan to retire: ", min_value=age+1)
    principal = get_positive_float("Enter your initial deposit amount: ")
    annual_savings = get_positive_float("Enter the amount you save each year: ")
    annual_interest_rate = get_positive_float("Enter the annual interest rate (in %): ") / 100

    # Compute investment duration
    years = retirement_age - age
    total_saved = annual_savings * years

    # Monthly compounding
    periods = 12  
    contribution = annual_savings / 12  

    # Progress indicator
    print("\n🔄 Calculating compound interest, please wait...\n")
    time.sleep(1)

    # Compute future value
    final_amount = compound_interest(principal, annual_interest_rate, periods, years, contribution)

    # Display results
    display_results(years, total_saved, final_amount)

if __name__ == "__main__":
    main()
