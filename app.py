import streamlit as st

def calculate_tax_rate(gross_salary, retention_rate):
    if gross_salary <= 12450:
        return retention_rate
    elif gross_salary <= 20200:
        return retention_rate
    elif gross_salary <= 35200:
        return retention_rate
    elif gross_salary <= 60000:
        return retention_rate
    else:
        return retention_rate

def update_living_cost(category, value):
    st.session_state[category] = value
    calculate_net_salary()

def update_gross_salary(value):
    st.session_state.gross_salary = value
    calculate_net_salary()

def update_retention_rate(value):
    st.session_state.retention_rate = value
    calculate_net_salary()

def calculate_net_salary():
    gross = st.session_state.gross_salary
    tax_percent = calculate_tax_rate(gross, st.session_state.retention_rate)

    net = gross * (1 - tax_percent / 100)

    living_cost = (
        st.session_state.rent
        + st.session_state.cars
        + st.session_state.groceries
        + st.session_state.cinema
        + st.session_state.other
        + st.session_state.investments
        + st.session_state.flight_savings
    )

    remaining_salary = net - living_cost

    st.write(f"Tax Percentage Applied (%): {tax_percent}")
    st.write(f"Net Salary after Taxes (€): {net:.2f}")
    st.write(f"Total Living Cost (€): {living_cost:.2f}")
    st.write(f"Remaining Salary after Living Costs (€): {remaining_salary:.2f}")


# Initialize session state variables
if "gross_salary" not in st.session_state:
    st.session_state.gross_salary = 30000
    st.session_state.retention_rate = 25
    st.session_state.rent = 1200
    st.session_state.cars = 600
    st.session_state.groceries = 800
    st.session_state.cinema = 100
    st.session_state.other = 300
    st.session_state.investments = 0
    st.session_state.flight_savings = 200

# Streamlit app layout
st.title("Net Salary Calculator in Spain")

# Gross Salary slider
st.write(f"Gross Salary (€): {st.session_state.gross_salary}")
gross_salary = st.slider("Adjust Gross Salary", 0, 100000, st.session_state.gross_salary, key="gross_salary")
update_gross_salary(gross_salary)

# Retention Rate slider
st.write(f"Retention Rate (%): {st.session_state.retention_rate}")
retention_rate = st.slider("Adjust Retention Rate", 0, 50, st.session_state.retention_rate, key="retention_rate")
update_retention_rate(retention_rate)

# Living Cost sliders
st.subheader("Living Cost Breakdown for a Family of 4 (€):")
for category in ["Rent", "2 Cars", "Groceries", "Cinema", "Other", "Investments", "Flight Tickets Savings"]:
    st.write(f"{category}: {st.session_state[category.lower().replace(' ', '_')]:.2f}")
    value = st.slider(f"Adjust {category}", 0, 2000, st.session_state[category.lower().replace(' ', '_')], key=category.lower().replace(' ', '_'))
    update_living_cost(category.lower().replace(' ', '_'), value)

# Calculate button
st.button("Calculate Net Salary", on_click=calculate_net_salary)
  
