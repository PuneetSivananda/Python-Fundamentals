set_a = {"one", "two", "three"}
print(set_a)

f_set_a = frozenset(set_a)
set_a.add("four")
print(set_a)

set_a.update(["five", "six","seven" ])
print(set_a)

set_a.remove("six")
print(set_a)

set_a.discard("seven")
print(set_a)

set_a.pop()
print(set_a)


print(f_set_a)