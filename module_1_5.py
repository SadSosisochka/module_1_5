immutable_var= 1,2,3.5,'строка',True
print(immutable_var)
print(immutable_var+1) #не поддерживает обращение по элементам, поддерживает только изменение списка если он есть внути,конкатенацию и умножение
mutable_list=[1,2,3]
mutable_list[0]=3
print(mutable_list)