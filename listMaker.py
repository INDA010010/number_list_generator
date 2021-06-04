num = int(input("Enter start number: "))
num2 = num
end = int(input("Enter end number: "))
output = ""
while num <= end:
    if num == num2:
        output += "["+str(num)+", "
        num += 1
    if num != num2 and num != end:
        output += str(num)+", "
        num += 1
    if num == end:
        output += str(num)+"]"
        break
print(output)
