num = int(input("Enter start number: "))
num2 = num
result = int(input("Enter end number: "))
while num <= result:
    if num == num2:
        print("[", str(num), ", ")
        num += 1
    if num != num2 and num <= result:
        print(str(num),", ")
        num += 1
    if num == result:
        print(str(num), "]")
        break
