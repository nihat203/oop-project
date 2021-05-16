class AliexpressScraper:
	def aliexpress_1(item,price_min,price_max,amazon,sortt):
			urls_1='https://aliexpress.ru/wholesale?catId=0&SearchText='+inputt
			if(price_min!=-1):
				urls_1+='&minPrice='+str(price_min)
			if(price_max!=-1):
				urls_1+='&maxPrice='+str(price_max)
			if(sortt!=''):
				urls_1+='&SortType='+sortt
			driver.get(urls_1)
			soup_1=BeautifulSoup(driver.page_source,'html.parser')
			def data_1(item_1):
				name_1=item_1.find('a',{'class': 'item-title'})['title']
				url_1=item_1.find('a',{'class': 'item-title'})['href']
				price_1=item_1.find('span','price-current')
				res_1=price_1.text+'&nbsp;'+'<a href=\"'+url_1+'\">'+name_1+'</a><br>';
				return res_1
			datas_1=[]
			res_1=soup_1.find_all('div',{'class': 'product-info'})
			s_1='<font size=\"+5\">aliexpress.ru</font><br>'
			for i_1 in res_1:
				s_1+=data_1(i_1)