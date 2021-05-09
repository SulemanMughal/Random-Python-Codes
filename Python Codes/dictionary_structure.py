tel = {'jack':4098, 'sape' :4139}
print(tel)
print(tel['jack'])
tel['guido'] = 4123
print(tel)
del tel['jack']

print(tel)
print(list(tel.keys()))
print(tel.keys())

print('guido' in tel)
A =dict(a = 1, b= 2)
print(A)

print(tel.items())
print(list(tel.items()))

for k,v in tel.items():
    print(k, v)
