# the list "meals" is already defined
# your code here
total = 0
for dict_ in meals:
    dict_ = dict(dict_)
    total += dict_["kcal"]
print(total)
