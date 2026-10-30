num = int(input("enter a number: "))
revrse_val = 0
digit = num
while digit!=0:
    n = digit%10
    revrse_val = revrse_val*10+ n
    digit  = digit//10
print("revresed number is: ", revrse_val)   
    