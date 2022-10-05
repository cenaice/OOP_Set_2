# file = open("nums.txt", 'r')
# data = file.readlines()
# count = 0
# for line in data:
#     s = line.split(' ')
#     count += s.count('1')
#     count += s.count('1\n')
# print(count)


#count = 0
#
#for line in sfile:
#
 #   if len( line.split() ) == 0:
#
 #       count += 1
#
#print(count)

#sfile.close()
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.get(2))
message = ""
for key, val in sales.items():
    message += f"{key}^{val} + "
print(message.strip(" + "))