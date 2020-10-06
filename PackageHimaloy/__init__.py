def createfile(filename, text):
    text = str(text)
    with open(f'D://Mydesktop/{filename}.txt', 'w') as fh:
        for i in range(1):
            fh.write(text)
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
class my_dictionary(dict):
    def add(self, key, value):
        self[value] = key
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
def hcf(num1, num2):
    num1, num2 = int(num1), int(num2)
    if num2 > num1:
        mn = num1
    else:
        mn = num2
    for i in range(1, mn + 1):
        if num1 % i == 0 and num2 % 1 == 0:
            hcf = i
    return hcf
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
def lcm(num1, num2):
    num1, num2 = int(num1), int(num2)
    maxnum = max(num1, num2)
    while True:
        if maxnum % num1 == 0 and maxnum % num2 == 0:
            break
        maxnum = maxnum + 1
    return maxnum
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
def interest(principle, rate, time=1,):
    """
    docstring
    """
    return principle*rate*time/100