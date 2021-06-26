
products = []
while True:
	name = input('please input product name:')
	if name == 'q':
		break
	price = input('please input product price:')
	price = int(price)
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

for p in products:
	print(p)          #p是在product裡的小清單
	print(p[0])       #印出小清單裡的[0]

#字串合併: 'abc' + '123' = 'abc123'

with open('products.csv', 'w', encoding='utf-8') as f: # 'r':read, 'w':write; with在這裡的功用是自動close檔案, 很多程式要手動關閉
	f.write('produce' + ',' + 'price' + '備註' + '\n')          # 使用utf-8編碼, 可以寫入中文字
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # ',' 是拿來區隔在excel開啟可以看到會分隔
		                                        # 因為 + 只能拿來用字串合併, 但price上面定義成int, 所以要用str()轉換
		                                        # '\n' 換行

