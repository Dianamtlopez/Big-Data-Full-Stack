roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}

rv = roman_value
for item in rv:
    print(item)
    
for item in rv.items():
    print(item)
    
for clave, valor in rv.items():
    print("{:>2}: {:>4}".format(clave, valor))