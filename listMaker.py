num = int(input("Enter start number: "))
result = int(input("Enter end number: "))
while num <= result:
    if num == num:
        print("[", str(num), ", ")
        num += 1
    if num != num and num <= result:
        print(str(num),", ")
        num += 1
    if num == result:
        print(str(num), "]")
        break
