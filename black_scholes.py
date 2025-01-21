
#implementing black scholes formula in python

import numpy as np
from scipy.stats import norm #because we need normal distribution

#define varibales
#this values are for tata motors options as of 19th december 2024

r = 0.055 #risk free interest rate
S = 745.75 #stock price
K = 760 #strike price
T = 0.0191 #time to maturity in years
sigma = 0.29 #annualized SD

#create function becuase we are going to use as many times as we wish
#type="C" means the call option

def blackScholes(r, S, K, T, sigma, type="C"):
    "Calculate BS option price for a call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) /(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "C":
            #as it is stand normal disrtibution it has mean = o, variance=1
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2,0,1)
        elif type == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2,0,1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("plz confirm all option paramters above!!!")
        
print("Option Price is: ", round(blackScholes(r, S, K, T, sigma, type="C"), 2)) #rounding off to 2 decimal places
#select type = "P for getting put price