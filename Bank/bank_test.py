# Define the function to calculate total interest
def calculate_interest(loan_amount, interest_rate, loan_period):
    """
    Calculates the total interest paid over the loan period.

    Args:
        loan_amount: The initial loan amount (principal) in baht.
        interest_rate: The annual interest rate as a percentage.
        loan_period: The loan period in years.

    Returns:
        The total interest paid in baht.
    """
    total_interest = loan_amount * (interest_rate / 100) * loan_period
    return total_interest

# Define the function to calculate monthly payment


def calculate_monthly_payment(loan_amount, total_interest, loan_period):
    """
    Calculates the monthly payment amount.

    Args:
        loan_amount: The initial loan amount (principal) in baht.
        total_interest: The total interest paid over the loan period in baht.
        loan_period: The loan period in years.

    Returns:
        The monthly payment amount in baht.
    """
    # Calculate the total number of payments (equal payments per year)
    total_payments = loan_period * 12
    monthly_payment = (loan_amount + total_interest) / total_payments
    return monthly_payment


# Example usage
loan_amount = 100000  # Loan amount in baht
interest_rate = 3  # Annual interest rate in percentage
loan_period = 2  # Loan period in years

# Calculate total interest
total_interest = calculate_interest(loan_amount, interest_rate, loan_period)

# Calculate monthly payment
monthly_payment = calculate_monthly_payment(
    loan_amount, total_interest, loan_period)

# Print the results
print("DPU Bank Loan Info")
print(f"Loan: {loan_amount:,.2f} baht")
print(f"Rate: {interest_rate:.2f}%")
print(f"Total Interest: {total_interest:.2f} baht")
print(f"Monthly Payment: {monthly_payment:.2f} baht")
