hrs = input("Enter Hours:")
rate = input('Enter Rate:')
r = float(rate)
h = float(hrs)

if h <= 40:
    gross_pay1 = h*r
    print(gross_pay1)
else:
    gross_pay2 = 40*r + (h-40)*(1.5*r)
    print(gross_pay2)
