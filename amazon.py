class AmazonScraper:
	def amazon_1(item,price_min,price_max,aliexpress,sortt):
			urls_2='https://www.amazon.com/s?k='+inputt

			if sortt=='price_asc':
				urls_2+='&s=price-asc-rank&ref=sr_st_price-asc-rank'
			if sortt=='price_desc':
				urls_2+='&s=price-desc-rank&ref=sr_st_price-desc-rank'
			if price_min!=-1:
				urls_2+='&low-price='+str(price_min)
			if price_max!=-1:
				urls_2+='&high-price='+str(price_max)
			driver1.get(urls_2)
			soup_2=BeautifulSoup(driver1.page_source,'html.parser')
			def data_2(item_2):
				ht_2=item_2.h2.a
				name_2=ht_2.text.strip()
				url_2='https://www.amazon.com'+ht_2.get('href')
				try:
					price_evvel_2=item_2.find('span','a-price')
					price_2=price_evvel_2.find('span','a-offscreen').text
				except AttributeError:
					return
				res_2=price_2+'&nbsp;'+'<a href=\"'+url_2+'\">'+name_2+'</a><br>';
				return res_2
			datas_2=[]
			res_2=soup_2.find_all('div',{'data-component-type': 's-search-result'})
			s_2="<font size=\"+5\">amazon.com</font><br>"
			for i_2 in res_2:
				temp_2=data_2(i_2)
				if(temp_2):
					s_2+=temp_2