import yfinance as yf
import pandas as pd

# Download data
data = yf.download("TATAMOTORS.NS", period="1y")

# Export to Excel
output_file = "TATA_MOTORS_DATA.xlsx"  # Define the output file name
data.to_excel(output_file)

print(f"Data has been exported to {output_file}")
