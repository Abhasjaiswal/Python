Dict={'Roll_No':'16/001','Name':'Arnav','Course':'B.tech'}
print(sorted(Dict.keys()))

print('KEYS: ',end= ' ')
for key in Dict:
    print(key,end=' ')
print("\n VALUES: ",end=' ')

for val in Dict.values():
     print(val,end=' ')
print("\nDICTIONARY: ",end=' ')
for key, val in Dict.items():
     print(key,val,'\t',end=' ')
     
students={'Bhavesh':{'CS':90,'DS':89,'CSA':'92'},
          'Rashika':{'CS':100,'DS':100,'CSA':100}}
for key,val in students.items():
     print(key,val)