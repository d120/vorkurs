list = [1, 2, 3, 4, 5]
# Da die Indices bei 0 anfangen ist len(list) - 1 der letzte gültige Index.
# ------------------------
index = 0
while index < len(list):
    print(list[index])
    index += 1
# ------------------------
for i in range(len(list)):
    print(list[i])
