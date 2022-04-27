print("Please select one of the following")
print("\n 1. Performance Measurement \n 2. Backtesting \n 3. Value Investing \n4. Trade using FXCM")
n =  int(input())
if n == 1:
    print("\n Performance Measurement using \n 1.CAGR \n 2. Volatility Measures \n 3. Sharpen and Sortino Ratio \n 4. Maximum Drawdown and Calmer Ratio")
    x = int(input())
    if x == 1:
        exec(open("cagr.py").read())
    elif x == 2:
        exec(open("volatility.py").read())
    elif x == 3:
        exec(open("sharp_shortino.py").read())
    elif x == 4:
        exec(open("calmer_ratio.py").read())
    else:
        print("Invalid choice")
elif n == 2:
    print("\n Backtest using \n 1.Portfolio Rebalancing \n 2. Resistance Breakout \n 3. Renko And OBV \n 4. Renko and MACD")
    x = int(input())
    if x == 1:
        exec(open("portfolio_backtesting.py").read())
    elif x == 2:
        exec(open("breakdown_bactesting.py").read())
    elif x == 3:
        exec(open("renko_obv.py").read())
    elif x == 4:
        exec(open("renko_macd.py").read())
    else:
        print("Invalid choice")
elif n == 3:
    print("\n Value Investing using \n 1.Magic Formula \n 2. Piotraski F-score ")
    x = int(input())
    if x == 1:
        exec(open("magic_for.py").read())
    elif x == 2:
        exec(open("piotraski_fscore.py").read())
    else:
        print("Invalid choice")
elif n == 4:
    print("\n Trading Using FXCM Terminal")
    exec(open("project.py").read())
else:
    print("Invalid choice")
