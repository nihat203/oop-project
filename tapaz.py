class TapazScraper:
	def tapaz_1(item,price_min,price_max,tapaz,sortt):
			urls_3='https://tap.az/elanlar?keywords='+inputt

			if sortt!='':
				urls_3+='&order='+sortt
			if price_min!=-1 and price_max!=-1:
				urls_3+='&q%5Bprice%5D%5B%5D='+str(price_min)+'&q%5Bprice%5D%5B%5D='+str(price_max)
			if price_min!=-1 and price_max==-1:
				urls_3+='&q%5Bprice%5D%5B%5D='+str(price_min)+'&q%5Bprice%5D%5B%5D='
			if price_min==-1 and price_max!=-1:
				urls_3+='&q%5Bprice%5D%5B%5D=&q%5Bprice%5D%5B%5D='+str(price_max)

			driver2.get(urls_3)
			soup_3=BeautifulSoup(driver2.page_source,'html.parser')
			def data_3(item_3):
				ht_3=item_3.find('a',{'class': 'products-link'})
				name_3=ht_3.find('div',{'class': 'products-name'})
				url_3='https://tap.az'+item_3.find('a',{'class': 'products-link'})['href']
				price_3=item_3.find('span','price-val')
				res_3=price_3.text+'AZN&nbsp;'+'<a href=\"'+url_3+'\">'+name_3.text+'</a><br>';
				return res_3
			datas_3=[]
			res_3=soup_3.find_all('div',{'class': 'products-i rounded'})
			s_3='<font size=\"+5\">tap.az</font><br>'
			for i_3 in res_3:
				s_3+=data_3(i_3)