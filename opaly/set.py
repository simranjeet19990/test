# now we dowing the difference b/w set & list
'''f={'b','b','a'} #set
print(f)
s=['b','b','a'] # list
print(s)
print(s[0])
s[2]='simran'
#print(f[0]) # this not working in set 
print(s)'''


drinks={"cola","sprite","beer","water","soda"}
print(drinks)
 #add  cell with 'soda' value 
drinks.add('soda')# agar ham jo pala sa ha set ma usa add kar ta ha to vo add nhi hoga 
print(drinks)
drinks.add('sime')
print(drinks)
s=drinks.copy()
print(s)
print("give me the lenght of the drinks variable",len(drinks))