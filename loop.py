#i = 0
#while i < 5:
#    i += 1
#    print(i)
#

#y = 0
#while y < 5:
#    y += 1
#    if y == 2:
#        break
#    print(y)


#z = 0
#while z < 5:
#    z += 1
#    if z == 2:
#        continue
#    print(z)

#for loop

#bicis = ['shimano','cannondale','kona','specialized','scott','swimm','francel']
#for i in bicis:
#    print(i)


#bicis = ['shimano','cannondale','kona','specialized','scott','swimm','francel']
#for bici in bicis:
#    if bici == 'scott':
#        continue
#    print(bici)

#for i in range(20,35,3):
#    print(i)
#else: // SE USA EN LOS FOR LOOPS
#    print('Print terminado')


bicis = ['shimano','cannondale','kona','specialized','scott','swimm','francel']
users = ['Luis','Pedro','Fran']

for bici in bicis:
    for user in users:
        if user == 'Pedro':
            continue
        print(bici,user)