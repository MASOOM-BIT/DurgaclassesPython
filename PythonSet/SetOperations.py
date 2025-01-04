#1. UNION() or | : To merge two sets , by default duplicate will be removed from final set also
#2. intersection() or & : return call elements present in both set

set1 = {10,20,30,40}
set2 = {100,200,300,400,40}

print(set1.union(set2))
print(set1|set2)

print(set1.intersection(set2))
print(set1&set2)

#3. difference or '-' :return the element present in i.e (s1-s2) , present in s1 but not in s2

print(set1.difference(set2))
print(set1-set2)

#4. Symmetric Difference (s1^s2): return element present in s1 but not in s2 and present in s2 but not in s1

print(set1.symmetric_difference(set2))
print(set1^set2)

#MEMBERSHIP in SETS

print(10 in set1)
print(10 not in set1)
print(444 in set1)

#SET COMPREHENSION

set3 = {x*x for x in range(1,21) if x%2==0}
print(set3)