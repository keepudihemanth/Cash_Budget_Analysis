import matplotlib.pyplot as plt

# Data from the report for FY 2022-23 and FY 2023-24
years = ['FY 2022-23', 'FY 2023-24']
opening_balance = [10510, 11997]   # in ₹ Cr
cash_inflows = [54280, 56700]      # in ₹ Cr
cash_outflows = [52793, 55300]     # in ₹ Cr

# Plotting the data
fig, ax = plt.subplots(figsize=(8, 5))

# Bar width
bar_width = 0.25
x = range(len(years))

# Plot bars for each category
bars1 = ax.bar([p - bar_width for p in x], opening_balance, width=bar_width, label='Opening Balance', color='blue')
bars2 = ax.bar(x, cash_inflows, width=bar_width, label='Cash Inflows', color='green')
bars3 = ax.bar([p + bar_width for p in x], cash_outflows, width=bar_width, label='Cash Outflows', color='red')

# Adding labels and title
ax.set_title('Cash Budget Analysis of HCL Tech (₹ Cr)', fontsize=14)
ax.set_xlabel('Financial Year', fontsize=12)
ax.set_ylabel('Amount (₹ Cr)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

# Function to add labels on top of each bar
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', 
                ha='center', va='bottom', fontsize=10, color='black')

# Adding the number labels to each group of bars
add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Display the plot
plt.show()
