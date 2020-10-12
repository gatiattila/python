#0. Hobby shopp.
#To be able to sell the latest article that was added to the shop
#To be able to sell any item that is in the shop
#To restock the shop with new items
article = 'scarf','gloves','trousers','shirt'
size = 'S','M','L','XL','XXL'
hobby_shop = [(x,y,z) for x in range(1,21) for y in article for z in size]
print(hobby_shop)
hobby_shop.pop()
if (1,'scarf','S') in hobby_shop:
    hobby_shop.remove((1,'scarf','S'))

print((len(hobby_shop)))
new_elem = [1,'scarf','S']
hobby_shop.insert((len(hobby_shop)),new_elem)
print(len(hobby_shop))
	
#1. Write a python code to remove an element from a tuple.

t = ("r","e","m","o","v","e","e","l","e","m","e","n","t")
t = t[:6] + t[7:]
print(t)

#2. Replace the last element in the list with the string 'last'
#using list comprehension and tuples
l=[lst for lst in t[:len(t)-1]]
l.append("last")
print(l)

#3. Extract only the strings from the following list using
#list comprehension :slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
slist = [ l for l in slist if type(l) == str ]
print(slist)

#4. Generate a 3 by 3 matrix that contains 'X'
#on the main diagonal and '_' in the rest.
matr = [ (x,y,z)
         for x in ['X','_']
         for y in ['X','_']
         for z in ['X','_']
         if ((x=='X' and y=='_' and z=='_')
             or (x=='_' and y=='_' and z=='X')
             or (x=='_' and y=='X' and z=='_'))]
print(matr[0])
print(matr[1])
print(matr[2])