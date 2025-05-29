## Temperature Conversion
def convert_temperature(temp, unit):
    """This function converts temperature between Celsius and Fahrenheit"""
    if unit == 'C':
        return temp * 9/5 + 32
    
    return (temp - 32)*5/9 

ans = convert_temperature(30, 'F')
print(ans)

## lambda function
addition = lambda a,b : a + b
print(addition(3, 5))