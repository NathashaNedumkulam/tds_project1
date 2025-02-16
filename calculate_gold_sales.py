import sqlite3

# File paths
db_file = "C:/Users/natha/tds_project1/data/ticket-sales.db"
output_file = "C:/Users/natha/tds_project1/data/ticket-sales-gold.txt"

# Connect to the database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Query to calculate total sales for "Gold" tickets
cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
total_sales = cursor.fetchone()[0]  # Fetch result

# Close the database connection
conn.close()

# Save result to file
with open(output_file, "w") as f:
    f.write(str(total_sales))

print(f"✅ Total sales for 'Gold' tickets saved to {output_file}")
