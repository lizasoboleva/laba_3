n=int(input("Введите номер места в плацкартном вагоне: "))
print()

if n%2==0 and n<=36:
    print('Ваше место - верхнее, купе.')
elif n%2!=0 and n<=35:
    print ('Ваше место - нижнее, купе.')
elif n%2==0 and n>36:
    print('Ваше место - верхнее, боковое.')
else:
    print('Ваше место - нижнее, боковое.')
