# temperature in degrees Fahrenheit
temperature_f = float(input('Please type temperature you want to convert :'))

temperature_c = float((temperature_f - 32) * 5.0 / 9.0)
print('Conversion is '+str(temperature_c))

# Compounding
P = 10000
n = 12
interest_rate = 0.08
t = int(input('Please insert the number of years :'))

Amount = float(P * (pow((1 + interest_rate / n), n * t)))
print('The final amount is :'+str(Amount))
