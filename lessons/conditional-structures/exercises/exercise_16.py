n = 2  # Do not modify this line... I will know if you do!
if n < 0:
    message = "The number is negative"
elif n > 0:
    message = "The number is positive"
else:
    message = "The number is zero"

if n%2 == 0:
    message += " and even"
else:
    message += " and odd"
