import numpy as np

## creating 1D array
arr1 = np.array([1, 2, 3, 4])
print(arr1)
print(type(arr1))
print(arr1.shape)

## Reshaping the array
arr2 = np.array([1, 2, 3, 5])

## Ones array
print(np.ones((3, 4)))

## vectorise operation
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print(" Addition : ", arr1 + arr2)
print(" Subtraction : ", arr2 - arr1)
print(" Multipilcation : ", arr1 * arr2)
