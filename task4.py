import rpy2.robjects as robjects

# Define an R function
robjects.r('''
    my_function <- function(x) {
        return(x * 2)
    }
''')

# Call the R function from Python
my_function = robjects.globalenv['my_function']
result = my_function(10)
print(result[0])  # Output: 20
library(reticulate)

# Import a Python module
os <- import("os")

# Use a Python function
current_directory <- os$getcwd()
print(current_directory)
# Python cell
import numpy as np
data = np.array([1, 2, 3, 4, 5])
print(data)
# R cell
data <- c(1, 2, 3, 4, 5)
print(data)
