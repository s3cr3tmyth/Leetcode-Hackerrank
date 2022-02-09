# n = 29
num = 30
# n = str(n)

# # print(n[1:])

# # if len(n) == 1:
# #     return str("Both")

# # if '0' in n:
# #     return False

# j = 0
# k = len(n)

# x1= []
# y1= []

# for idx, _ in enumerate(n):
#     # n.pop(j)
#     x = n[j:]
#     x1.append(x)
#     y = n[:k]
#     y1.append(y)
#     j+=1
#     k-=1

# # print(x1)
# # print(y1)

# for i in x1:
#     for j in y1:
#         if (is_prime(int(i)) == True):
#             print('right')
#         elif (is_prime(int(j)) == True):
#             print('left')
#         elif (is_prime(int(j)) == True and is_prime(int(i)) == True):
#             print('both')
#         else:
#             print('False')


# def is_prime(num):
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            # return True
            break
    else:
        print(num, "is a prime number")
             # return False

