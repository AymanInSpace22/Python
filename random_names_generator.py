import names

count = 0
for i in range(15):
    count += 1
    print(str(count) + '.', names.get_full_name())
