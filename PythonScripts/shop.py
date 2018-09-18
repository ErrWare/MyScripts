
import webbrowser
import requests
import json
# SPROUTS:
file = open('sproutsHeader.json','r')
headers = json.loads(file.read())
file.close()
sprouts_produce = 'https://shop.sprouts.com/api/v2/store_products?_nocache=1536272806020&category_id=1&limit=90&offset=0&sort=price_low&tags=on_sale'
sprouts_bulk = 'https://shop.sprouts.com/api/v2/store_products?_nocache=1536280340189&category_id=103&limit=90&offset=0&sort=price_low&tags=on_sale'
sprouts_meat = 'https://shop.sprouts.com/api/v2/store_products?_nocache=1536280418827&category_id=67&limit=60&offset=0&sort=price_low&tags=on_sale'
sprouts_dict = {
	'produce':{
		'url':'https://shop.sprouts.com/api/v2/store_products?_nocache=1536272806020&category_id=1&limit=90&offset=0&sort=price_low&tags=on_sale',
		'keywords':['kale','pine','onion','sweet','hass','garlic']
	},
	'bulk':{
		'url':'https://shop.sprouts.com/api/v2/store_products?_nocache=1536280340189&category_id=103&limit=90&offset=0&sort=price_low&tags=on_sale',
		'keywords':['blanched','oat']
	},
	'meat':{
		'url':'https://shop.sprouts.com/api/v2/store_products?_nocache=1536280418827&category_id=67&limit=60&offset=0&sort=price_low&tags=on_sale',
		'keywords':['chicken','rib']
	}
}

key_col_format = {
	'name':'{0:<20s}',
	'sale_price':'{0:2.2f}',
	'promo_tag':'{0:12s}',
	'sale_end_date':'{0:5s}'
}
def printSproutsHeader(section):
	print('~~~'+section.capitalize())
	print('{0:^20s}\t{1:^5s}\t{2:^12s}\t{3:^5s}'.format('Product Name','sale$','promo','end'))

def printSproutsItem(i):
	# Represent day as 'MM-DD'
	if len(i['name']) > 20:
		i['name'] = i['name'][-20:].strip()
	i['sale_end_date'] = i['sale_end_date'][5:10]
	for key, format in key_col_format.items():
		print(format.format(i[key]), end='\t')
	print()

print('~'*22 + ' SPROUTS ' + '~'*22)
for section, info in sprouts_dict.items():
	res = requests.get(info['url'],headers=headers)
	try:
		res.raise_for_status()
	except:
		message = 'Failure loading section: ' + section
		print('~'*(len(message)+6))
		print('~~ ' + message + ' ~~')
		print('~'*(len(message)+6))
		continue
	dic = json.loads(res.text)
	printSproutsHeader(section)
	for item in dic['items']:
		for keyword in info['keywords']:
			if keyword in item['name'].lower():	
				printSproutsItem(item)
				break
	print()



input()
'''
webbrowser.open('https://shop.sprouts.com/shop/categories/1?tags=on_sale&sort=price_low')
webbrowser.open('https://shop.sprouts.com/shop/categories/103?tags=on_sale&sort=price_low')
webbrowser.open('https://shop.sprouts.com/shop/categories/67?tags=on_sale&sort=price_low')
webbrowser.open_new_tab('https://coupons.tomthumb.com/weeklyad/?store=2526&s=')
'''