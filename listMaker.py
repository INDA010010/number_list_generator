num = int(input("Enter start number: "))
result = int(input("Enter end number: "))
while num <= result:
    if num == 1:
        print("[", str(num), ", ")
        num += 1
    if num != 1 and num <= result:
        print(str(num),", ")
        num += 1
    if num == result:
        print(str(num), "]")
        break
