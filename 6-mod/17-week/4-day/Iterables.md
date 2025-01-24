# Iterables

- Data **_category_** for loopables
- Can be passed to `iter()`
  - Use `next()` to iterate

```py
names = ['Zaviar', 'Seika', 'Eiki']
pets = {
    'Zaviar': ['Momo', "Tenten", 'Kiki'],
    'Seika': ['Tora', 'Sonic', 'Dragon'],
    'Eiki': ['Hime', 'Koga']
}
name_iter = iter(names)
pet_iter = iter(pets)

print(name_iter)
print(pet_iter)

print(next(name_iter))
print(next(pet_iter))
```
