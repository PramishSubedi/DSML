def calculate_emi(principal, annual_rate, years):
    """
    Calculate monthly EMI for a loan.
    """
    monthly_rate = annual_rate / (12 * 100)

    months = years * 12

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

    return emi