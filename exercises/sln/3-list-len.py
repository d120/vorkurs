list_ = [1, 2, 3, 4, 5]
# Da die Indices bei 0 anfangen ist len(list_) - 1 der letzte gültige Index.
# ------------------------
index = 0
while index < len(list_):
    print(list_[index])
    index += 1
# ------------------------
for i in range(len(list_)):
    print(list_[i])
