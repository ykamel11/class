
try:
        gross = input("gross amount")
        children = input("number of children")
        gross = int(gross)
        children = int(children)

except:
    print("please use proper numbers")
    percentage = 0

if gross<1000:
    percentage = 10 - children
elif gross<2000:
    percentage = 12 - children
elif gross<4000:
    percentage = 14 - children
else:
    percentage = 18-children*0.5

net = ((100-percentage)/100)*gross
print(net)
