def dollarizer(word):    
    return word.replace('s','$')

print(f"Dollarizer: {dollarizer('testcase')}")

def eurizer(word):   
    return word.replace('e','€')

print(f"Eurizer: {eurizer('testcase')}")

def replacer(word, char1, char2):    
    return word.replace(char1, char2)

print(f"Replace: {replacer('testcase', 't', '#')}")

def wonky_text(word):
    word = dollarizer(word)
    word = eurizer(word)
    return word.replace('I', '£')

print(f"Wonky Text: {wonky_text('testcase')}")

def celsius_to_fahrenheit(temp):
    return temp * 9/5 + 32

print(f"Celcius to Fahrenheit: {celsius_to_fahrenheit(25)}")

def age_in_days(age):
    return age * 365

print(f"Age in Days: {age_in_days(25)}")

def simple_interest(principal, interest, time):
    return principal * interest * time

print(f"Simple Interest: {simple_interest(10, 5.0, 5)}")

def plan_finances(principal, interest, time, final):
    correct_final = principal * interest * time
    return correct_final == final

print(f"Plan Finances: {plan_finances(10, 5.0, 5, 300)}")
    