#-----------definition and property of sets.
#set is a data structure used to store unique values in curly{}.
#sets are mutable in nature.
#sets does not support indexing,slicing and sequence.
#sets always recognize unique values.
#sets can be homogeneous and heterogeneous.



#creation of sets.
#empty set=set()
days={"monday","tuesday","wednesday"}
print(type(days))

#in-built methods(S.A)
#add
#intersect()
#difference()
#subset()
#superset()
#union

#adding
#my_set={1,3,4,5,6}
#my_set.add(9)
#print(my_set)

#intersect
my_set1={1,2,3,4,5}
my_set2={3,4,5,6,7}
intersect_num=my_set1.intersection(my_set2)
print(intersect_num)

#difference
set1={1,2,3,4,5}
set2={4,5,6,7,8}
difference_num=set1.intersection(set2)
print(difference_num)

#subset
set1={1,2,3,4,5,6,7}
set2={1,2,3}
print(set2.issubset(set1))
print(set1.issubset(set2))

#superset
set1={1,2,3,4,5,6}
set2={1,2,3}
print(set2.issuperset(set1))
print(set1.issuperset(set2))

#union
num1={1,2,3,4,5,6}
num2={4,5,6,7}
union_num=num1.union(num2)
print(union_num)