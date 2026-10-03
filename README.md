# Crypto Trade Risk Checker

A beginner-friendly Python command-line application that evaluates the risk level of a cryptocurrency trade based on price risk, market sentiment, and trader experience.

## Features

* Calculate stop-loss risk percentage
* Analyze market sentiment
* Consider trader experience level
* Calculate a total risk score
* Classify trades into:

  * Low Risk
  * Medium Risk
  * High Risk
* Display a simple trade risk summary

## Technologies Used

* Python
* No external libraries

## Python Concepts Practiced

This project was created to practice Python fundamentals learned from Google's Crash Course on Python.

* Variables
* Data types
* User input
* Type conversion
* Arithmetic operators
* Comparison operators
* Logical operators
* Functions
* Function parameters
* Return values
* `if / elif / else` statements
* Basic calculations

## How It Works

The program collects the following information from the user:

1. Cryptocurrency name
2. Current price
3. Entry price
4. Stop-loss price
5. Market sentiment
6. Trader experience level

The program then calculates the stop-loss risk percentage and combines it with market sentiment and experience level to produce a total risk score.

Finally, the trade is classified as **Low**, **Medium**, or **High Risk**.

## Risk Calculation

The stop-loss risk percentage is calculated using:

```text
Risk Percentage = (Entry Price - Stop Loss) / Entry Price × 100
```

The program uses this percentage to determine the price risk score.

## Example

```text
Enter cryptocurrency: Bitcoin
Enter current price: 65000
Enter entry price: 64000
Enter stop loss price: 62000
Enter market sentiment: bearish
Enter your experience level: beginner

----- RESULT -----

Crypto Name: Bitcoin
Current Price: 65000.0
Entry Price: 64000.0
Stop Loss: 62000.0
Risk Percentage: 3.12%
Risk Level: High
```

## Project Purpose

This project was created as a beginner Python project to practice programming fundamentals and apply them to a cryptocurrency-related problem.

It is also part of my learning journey while studying Python and exploring AI, cryptocurrency, and multi-agent systems.

## Future Improvements

Possible future improvements include:

* Add input validation
* Add loops for multiple trade analysis
* Store multiple trades using lists
* Use dictionaries to organize trade information
* Save trade results to a file
* Add cryptocurrency price data using an API
* Add a graphical user interface
* Add real-time cryptocurrency market data

## Project Structure

```text
crypto-trade-risk-checker/
│
├── risk_checker.py
├── README.md
└── .gitignore
```

## Author

Chamuditha Bandara

ICT Undergraduate Student
Rajarata University of Sri Lanka
