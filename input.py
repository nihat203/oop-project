class User_input
	def __init__():
		get_input()

	def get_input()
		#Errors
		inputt=request.form['text']
		if(inputt==''):
			return render_template('input.html')+'Search must not be empty!'

		names=request.form.getlist("sites")
		if not names:
			return render_template('input.html')+'You must at least pick one website!'

		price_min=request.form['price_min']

		try:
			if(price_min!=''):
				price_min=int(price_min)
			else:
				price_min=-1
		except:
			return render_template('input.html')+'Price must be number!'

		price_max=request.form['price_max']

		try:
			if(price_max!=''):
				price_max=int(price_max)
			else:
				price_max=-1
		except:
			return render_template('input.html')+'Price must be number!'

		if(price_max<price_min and price_max!=-1 and price_min!=-1):
			return render_template('input.html')+'Maximum price needs to be larger than minimum!'

		sortt=request.form['sort']
		sortt=str(sortt)
		
		

		aliexpress=0
		amazon=0
		tapaz=0
		Webscraper=1

		for i in range(0,len(names)):
			if names[i]=='amazon':
				amazon=1
			if names[i]=='aliexpress':
				aliexpress=1
			if names[i]=='tapaz':
				tapaz=1