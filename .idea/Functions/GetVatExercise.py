def get_vat(price, vat):
    return (price * vat) / 100


# Calling the function
vat = get_vat(200, 5)
print(vat)