
products = []
while True:
	name = input('please input product name:')
	if name == 'q':
		break
	price = input('please input product price:')
	#p=[]
	#p.append(name)
	#p.append(price)
	#products.append(p)
    #快寫1: p = [name, price]
    #快寫2: product.append([name, price])
	products.append([name, price])



# product [ name1.price1 ; name2.price2 ; ...] 大清單裡包小清單
print(products)
print(products[0][0])
#products[0][0] -> name1
#products[0][1] -> price1
#products[1][0] -> name2
#products[1][1] -> price2

