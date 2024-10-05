# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.

# Example: This time I have registered the speed of 7 cars:
# Use the Numpy std() method to find the standard deviation:

import numpy
speed = [86, 87, 88, 89, 90, 91]
x = numpy.std(speed)
print(x)  # prints 1.707825127659933

speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.std(speed)
print(x)  # prints 37.84501153334721

# Variance
# if you multiply the standard deviation by itself, you get the variance!
# To calculate the variance you have to do as follows:
# 1- Find the mean
# 2- For each value: find the difference from the mean
# 3- For each difference: find the square value
# 4- The variance is the average number of these squared differences

speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.var(speed)
print(x)  # prints 1432.2448979591834

# Symbols
# Standard Deviation is often represented by the symbol Sigma: σ
# Variance is often represented by the symbol Sigma Squared: σ2

