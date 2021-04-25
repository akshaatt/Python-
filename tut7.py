s1 = set()
# print(s1)
s_from_list = set([1, 2, 3, 4, 5])
print(s_from_list)
print(type(s_from_list))

s1.add(1)
s1.add(2)

s2 = s1.union({1, 2, 3, 4})
print(s2, s1)

s2 = s1.intersection({1, 2, 3, 4})
print(s2, s1)