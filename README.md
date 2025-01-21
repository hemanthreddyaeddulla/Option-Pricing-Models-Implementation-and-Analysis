# Option-Pricing-Models-Implementation-and-Analysis
This academic project implements and analyzes two fundamental option pricing models: the Black-Scholes model and the Binomial model. The implementation includes both Python and Excel-based calculations for European options, along with the computation of option Greeks. The project utilizes real market data from Tata Motors and Kotak Bank to demonstrate practical applications of these theoretical models.

### 1. Introduction
#### 1.1 Project Overview
The project focuses on implementing and comparing two widely used option pricing models:
- Black-Scholes Option Pricing Model
- Binomial Option Pricing Model

Additionally, the project includes the calculation of option Greeks to understand the sensitivity of option prices to various market parameters.

#### 1.2 Project Objectives
- Implementation of Black-Scholes and Binomial option pricing models in both Python and Excel
- Retrieval and processing of real market data using yfinance
- Calculation and analysis of option Greeks
- Comparative analysis of theoretical and market prices

### 2. Theoretical Background
#### 2.1 Black-Scholes Model
The Black-Scholes model is a mathematical model used for pricing European-style options. The model assumes:
- European-style options
- No dividends
- Constant risk-free rate
- Log-normal distribution of stock prices
- No transaction costs

#### 2.2 Binomial Model
The Binomial model is a discrete-time model that maps the possible paths that might be followed by the stock price over the option's life.

#### 2.3 Option Greeks
The project calculates five primary Greeks:
- Delta: Measures the rate of change in option value with respect to underlying asset price
- Gamma: Measures the rate of change in Delta with respect to underlying asset price
- Theta: Measures the rate of change in option value with respect to time
- Vega: Measures sensitivity to volatility
- Rho: Measures sensitivity to interest rate changes

### 3. Methodology
#### 3.1 Data Collection
- Used yfinance library to retrieve one year of historical data for Tata Motors
- Data exported to Excel for further analysis
- Separate data collection for Kotak Bank

#### 3.2 Implementation Tools
- Python (Jupyter Notebook)
- Excel
- Libraries: yfinance, numpy, pandas

#### 3.3 Input Parameters
##### Tata Motors (as of December 19, 2024)
- Stock Price: ₹745.75
- Strike Price: ₹760
- Expiry Date: December 26, 2024
- Risk-free Rate: 5.50%
- Volatility: 29.42%

##### Kotak Bank (as of January 20, 2025)
- Stock Price: ₹1,918
- Strike Price: ₹1,960
- Expiry Date: January 30, 2025
- Risk-free Rate: 7.0%
- Volatility: 24%

### 4. Implementation Details
#### 4.1 Project Structure
1. `tata_motors_1yr_data.py`
   - Data retrieval script for Tata Motors
   - Export functionality to Excel

2. `Option Pricing.xlsx`
   - Black-Scholes calculations
   - Binomial model implementation
   - Comparative analysis

3. `Binomial_Option_Pricing_Model.ipynb`
   - Python implementation of Binomial model for Kotak Bank

4. `Calculating_Option_Greeks_using_Black_Scholes_with_Python.ipynb`
   - Implementation of Greeks calculations

### 5. Results and Analysis
#### 5.1 Model Comparison
- No significant differences observed between Black-Scholes and Binomial model results
- Theoretical vs. practical value analysis performed to determine option valuation status (overvalued/undervalued)

#### 5.2 Greeks Analysis
Implementation and calculation of:
- Delta
- Gamma
- Theta
- Vega
- Rho

### 6. Limitations and Assumptions
- European-style options only
- No dividend consideration
- Constant volatility assumption
- Perfect market conditions assumed
- No transaction costs considered

### 7. Conclusion
The project successfully implemented both Black-Scholes and Binomial option pricing models, demonstrating their application with real market data. The consistency between both models validates the implementation accuracy. The addition of Greeks calculations provides deeper insights into option price sensitivities.

### 8. Future Scope
Potential areas for expansion:
- Implementation of American-style options
- Inclusion of dividend considerations
- Sensitivity analysis of Greeks
- Implementation of more advanced option pricing models
- Integration of real-time market data
- Addition of volatility surface analysis
