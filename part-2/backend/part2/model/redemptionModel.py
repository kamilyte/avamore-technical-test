from datetime import datetime, timedelta

# calculation of the total interest due
def interest_due(date_of_loan, redemption_date, facility_a, facility_b, facility_c, arrangement_fee, monthly_rate, interest_rate, beginning_default_period, end_default_period, drawdowns, capital_repayments):
    
    # input calculations
    interest_retention = facility_c - arrangement_fee
    daily_reg_rate = (monthly_rate / 30) / 100 
    annual_reg_rate = ((1 + daily_reg_rate)**365 - 1)
    daily_default_rate = (interest_rate / 30) / 100
    
    # initial calculations of the first date
    opening_pb = facility_a + arrangement_fee
    interest_balance = interest_retention
    drawdown = 0
    if date_of_loan in drawdowns:
        drawdown = drawdowns[date_of_loan]
    
    default_on = 0
    if (date_of_loan >= beginning_default_period and date_of_loan <= end_default_period) or (date_of_loan == datetime(1999, 12, 30)):
        default_on = 1

    if default_on == 1:
        daily_interest = (opening_pb + drawdown + interest_balance) * daily_default_rate
    else:
        daily_interest = (opening_pb + drawdown + interest_balance) * daily_reg_rate 
    
    payments_received = 0
    if date_of_loan in capital_repayments:
        payments_received = - capital_repayments[date_of_loan]
        
    closing_pb = opening_pb + drawdown + payments_received
    
    accrued_daily_interest = daily_interest
    
    # caclulating interest due for each day until the last day is reached
    while date_of_loan < redemption_date:
        date_of_loan = date_of_loan + timedelta(days=1)
        opening_pb = closing_pb
        interest_balance = max(accrued_daily_interest, interest_retention)
        
        drawdown = 0
        if date_of_loan in drawdowns:
            drawdown = drawdowns[date_of_loan]

        default_on = 0 
        if (date_of_loan >= beginning_default_period and date_of_loan <= end_default_period) or (date_of_loan == datetime(1999, 12, 30)):
            default_on = 1

        if default_on == 1:
            daily_interest = (opening_pb + drawdown + interest_balance) * daily_default_rate
        else:
            daily_interest = (opening_pb + drawdown + interest_balance) * daily_reg_rate 
        
        payments_received = 0
        if date_of_loan in capital_repayments:
            payments_received = - capital_repayments[date_of_loan]
            
        closing_pb = opening_pb + drawdown + payments_received
        
        accrued_daily_interest = daily_interest + accrued_daily_interest
    
    return int(round(accrued_daily_interest, 0))


def redemption_model(facility_a, monthly_rate, beginning_default_period, end_default_period):
    
    # original loan inputs that are not flexible
    date_of_loan = datetime(2023, 1, 15)
    redemption_date = datetime(2024, 4, 23)
    facility_b = 250000
    facility_c = 25000
    arrangement_fee = 5000
    interest_rate = 2
    
    # converting default periods to datetime for easier data handling
    beginning_default_period = datetime.strptime(beginning_default_period, "%d-%b-%y")
    end_default_period = datetime.strptime(end_default_period, "%d-%b-%y")
    
    # dictionary of drawdowns for quick search
    drawdowns = {
        datetime(2023, 2, 14): 25000,
        datetime(2023, 3, 25): 25000,
        datetime(2023, 5, 3): 25000,
        datetime(2023, 6, 11): 25000,
        datetime(2023, 7, 20): 25000,
        datetime(2023, 8, 28): 25000,
        datetime(2023, 10, 6): 25000,
        datetime(2023, 11, 14): 25000,
        datetime(2023, 12, 23): 25000,
        datetime(2024, 1, 31): 25000,
    }
    
    # dictionary of capital repayments for quick search
    capital_repayments = {
        datetime(2024, 2, 23): 100000
    }
    
    # calculate total interest due
    total_interest_due = interest_due(date_of_loan, redemption_date, facility_a, facility_b, facility_c, arrangement_fee, monthly_rate, interest_rate, beginning_default_period, end_default_period, drawdowns, capital_repayments)
    
    return total_interest_due