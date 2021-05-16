from scraper import scraper
class Showres
	def results(item,sortt,aliexpress,tapaz,amazon,price_min,price_max)
		res=results()
		final_result=res.tapaz+res.aliexpress+res.amazon
		return render_template('input.html')+final_result
