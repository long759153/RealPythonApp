def greater():
    print('hello')

def newGreater():
    print('hello, again')

def greaterSomeone(name):
    print('hello,'+ name)

name_1 = 'Lion'
greater()
newGreater()

greaterSomeone(name_1)

pets = ['dog','cat','bird','rabit','snake']

for pet in pets:
    print(pet)

head_1 = 'something new'
print(head_1)

completed_orderList = []

def order_Food(food_list, completed_orderList):
	while food_list:
		current_order = food_list.pop()
		print('now, I am ordering '+current_order)
		completed_orderList.append(current_order)
		
		


def printMyOrder(orderList):
	print('the food has been ordered as below:')
	for food in orderList:
		print(food)		
myfood = ['burger','chips','steak','bread','pastar']

order_Food(myfood, completed_orderList)
printMyOrder(completed_orderList)

