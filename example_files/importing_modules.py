#THIS FILE CONTAINS EXAMPLES OF HOW TO USE MODULES

#IMPORT A MODULE
import statistics
monthly_failed_attempts = [2, 3, 5, 1, 4, 2, 3]
mean_failed_attempts = statistics.mean(monthly_failed_attempts)
median_failed_attempts = statistics.median(monthly_failed_attempts)
print("Mean failed attempts:", mean_failed_attempts)
print("Median failed attempts:", median_failed_attempts)

#IMPORT A SPECIFIC FUNCTION FROM A MODULE
from statistics import mean, median
monthly_failed_attempts = [2, 3, 5, 1, 4, 2, 3]
mean_failed_attempts = mean(monthly_failed_attempts)
median_failed_attempts = median(monthly_failed_attempts)
print("Mean failed attempts (imported):", mean_failed_attempts)
print("Median failed attempts (imported):", median_failed_attempts)

#EXTERNAL lIBRARY (MUST BE INSTALLED FIRST)
import numpy as np
failed_attempts_array = np.array(monthly_failed_attempts)
print("Numpy array of failed attempts:", failed_attempts_array)