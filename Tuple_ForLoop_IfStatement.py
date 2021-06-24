tup = ('Sunday', 'Monday', 'Tuesday')

x = 0
for t in tup:
  x += 1
  if x == 1:
    print(f'The {x}st day of the week is',t)
  elif x == 2:
    print(f'The {x}nd day of the week is',t)
  else:
      print(f'The {x}rd day of the week is',t)
