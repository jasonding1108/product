
import os #operation system

def read_file(filename):
	products = []
 #讀取現有檔案
	with open(filename, 'r', encoding='utf-8') as f: #'r':read, 'w':write
		for line in f:
			if 'product,price' in line:  #只要認到'product,price'就跳到下一回, 也就是這個字串不會被載入; break是跳出迴圈
				continue
			name, price = line.strip().split(',') #切割分隔
			products.append([name, price]) #加入product裡
		return products

def user_input(products):
	#讓使用者輸入
	while True:
		name = input('please input product name:')
		if name == 'q':
			break
		price = input('please input product price:')
		price = int(price)
		products.append([name, price])
	return products

def print_product(products):
	for p in products:
		print(p[0], 'the price is', p[1])

def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: 
		f.write('product' + ',' + 'price' + '\n')          
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') 

#--------------------------------------------------------------------------------------------#

def main():
	products = []
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yes, found the file')
		products = read_file(filename)
	else:
		print('no, can not found the file')
	products = user_input(products)
	print_product(products)
	write_file(filename, products)

main()
