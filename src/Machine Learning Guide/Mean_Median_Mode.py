# Mean - The average value
# Median - The mid-point value
# Mode - The most common value
import numpy
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)
print(x)  # prints 89.76923076923077

# Median
x = numpy.median(speed)
print(x)  # prints 87

# Mode
x = stats.mode(speed)
print(x)  # prints ModeResult(mode=np.int64(86), count=np.int64(3))
