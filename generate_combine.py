from db import execute_query,execute_query2,execute_query3
from visual import generate_combined

def generate_data(chart_type,userid):
    
    chart_type=chart_type

    # Fetch data for daily report
    query_daily = """
    SELECT SUM(calories) AS total_sum, 
           TO_CHAR(entry_date, 'DD-MM') AS entry_date
    FROM calorie_entries 
    WHERE userid=%s
    GROUP BY TO_CHAR(entry_date,'DD-MM'), entry_date
    ORDER BY TO_CHAR(entry_date,'MM-DD') DESC
    LIMIT 7;
    """
    values_daily = (userid,)
    result_daily = execute_query(query_daily, values_daily)

    # Fetch data for weekly report
    query_weekly = """
    SELECT AVG(calories) AS average_weekly_calories,
           TO_CHAR(DATE_TRUNC('week', entry_date), 'DD-MM') AS start_of_week     
    FROM calorie_entries
    WHERE userid = %s
    GROUP BY TO_CHAR(DATE_TRUNC('week', entry_date), 'DD-MM')
    ORDER BY TO_DATE(TO_CHAR(DATE_TRUNC('week', entry_date), 'DD-MM'), 'DD-MM') ;
    """
    values_weekly = (userid,)
    result_weekly = execute_query(query_weekly, values_weekly)

    # Fetch data for monthly report
    query_monthly = """
    SELECT AVG(calories) AS monthly_calories,
           TO_CHAR(DATE_TRUNC('month', entry_date), 'DD-MM') AS start_of_month 
    FROM calorie_entries
    WHERE userid = %s
    GROUP BY TO_CHAR(DATE_TRUNC('month', entry_date), 'DD-MM')
    ORDER BY start_of_month;
    """
    values_monthly = (userid,)
    result_monthly = execute_query(query_monthly, values_monthly)

    # Generate combined plot
    generate_combined(result_daily, result_weekly, result_monthly, chart_type)

