class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            #print ("while "+ roman_num, num, val[i] , i)
            #print (num, val[i])
            for _ in range(num // val[i]):
                roman_num += syb[i]
                #print ("for "+ roman_num, num, val[i] , i)
                num -= val[i]
            i += 1
        return roman_num



print(py_solution().int_to_Roman(11))
print(py_solution().int_to_Roman(4000))