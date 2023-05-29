import random
lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
number = "0987654321"
symbols = "[](){},./#@^&+=-_:;!~`"

all = upper+lower+number+symbols
length=int(input("length : "))
password="".join(random.sample(all,length))
print(password)