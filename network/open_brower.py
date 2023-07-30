import webbrowser




# webbrowser.get(browser).open(url)
# browser = 'google-chrome'

# open default brower
def open_product_detail(id_product):
	url = f'http://127.0.0.1:8000/detail2/{id_product}'
	webbrowser.open(url=url, new=2)