def calculate_risk_percentage(entry_price, stop_loss):
    return (entry_price - stop_loss) / entry_price * 100
#function to calculate risk percentage based on entry price and stop loss

def check_risk_level(risk_percentage):
    if risk_percentage < 3:
        return 1
    elif 3 <= risk_percentage < 5:
        return 2
    else:
        return 3
#function to check risk level based on risk percentage

def check_market_risk(sentiment):
    if sentiment == "bearish":
        return 3
    elif sentiment == "neutral":
        return 2
    else:
        return 1
#function to check market risk based on sentiment

def check_experience_risk(experience):
    if experience == "beginner":
        return 3
    elif experience == "intermediate":
        return 2
    else:
        return 1
#function to check experience risk based on experience level

def determine_risk(total_score):
    if total_score >= 8:
        return "High"
    elif  total_score >= 6:
        return "Medium"
    else:
        return "Low"
#function to determine the overall risk based on the total score

print("==============================================")
print("             crypto trade risk checker")
print("==============================================")
#display apps name

crypto = input("Enter the crypto name: ")
#take crypto name as input from user

current_price = float(input("Enter the current price: "))
#take current price as input from user

entry_price = float(input("Enter the entry price: "))
#take entry price as input from user

stop_loss = float(input("Enter the stop loss price: "))
#take stop loss price as input from user

sentiment = input("Enter the sentiment (bullish/bearish/neutral): ")
#take sentiment as input from user

experience = input("Enter your experience level (beginner/intermediate/experienced): ")
#take experience level as input from user



risk_percentage = calculate_risk_percentage(entry_price, stop_loss)
#call the risk percentage function to calculate the risk percentage based on entry price and stop loss

price_risk = check_risk_level(risk_percentage)
#call the risk level function to check the risk level based on the calculated risk percentage

market_risk = check_market_risk(sentiment)
#call the market risk function to check the market risk based on the sentiment

experience_risk = check_experience_risk(experience)
#call the experience risk function to check the experience risk based on the experience level

total_score = price_risk + market_risk + experience_risk
#calculate the total score based on price risk, market risk, and experience risk   

risk_level = determine_risk(total_score)
#calculate the overall risk level based on the total score

print()
print("==============================================")
print("               RESULT")
print("==============================================")
print("Crypto Name: ", crypto)      
print("Current Price: ", current_price)
print("Entry Price: ", entry_price)
print("Stop Loss Price: ", stop_loss)
print("Risk Percentage: ", round(risk_percentage, 2), "%")
print("Risk Level: ", risk_level)