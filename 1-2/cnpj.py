def cleanCnpj(cnpj):
    cnpj = cnpj.replace(".","")
    cnpj = cnpj.replace("/","")
    cnpj = cnpj.replace("-","")
    return cnpj

# 1) Validate CNPJ Format (Mask)
def looksLikeCnpj(cnpj):

    cnpj = cleanCnpj(cnpj)
    
    if(len(cnpj) != 14):
        return False
    
    if(not cnpj.isnumeric()):
        return False
    
    return True

def validation_calc(digits, validation_digits):
    sum_digits = 0
    for i in range(len(digits)):
        sum_digits += int(digits[i])*validation_digits[i]
    
    sum_digits %= 11

    if(sum_digits < 2):
        digit = 0
    else:
        digit = 11 - sum_digits

    digit = str(digit)

    return digit

# 2) Validate CNPJ Digits
def validate(cnpj):

    cnpj = cleanCnpj(cnpj)

    if(not looksLikeCnpj(cnpj)):
        return False

    if(cnpj[0]*14 == cnpj):
        return False

    digits = cnpj[:12]

    validation_digits1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    validation_digits2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    digit1 = validation_calc(digits, validation_digits1)
    digits += digit1
    digit2 = validation_calc(digits, validation_digits2)
    digits += digit2

    if(digits == cnpj): return True
    else: return False

print("Kaffa Mobile CNPJ is valid: ", validate('08.730.563/0001-47'))
print("Other CNPJ: ", validate('69.435.154/0001-01'))