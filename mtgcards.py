import scrapy


class CKSpider(scrapy.Spider):
	name = 'mtgcards'

	def __init__(self, search_by, name, **kwargs):
		super().__init__(**kwargs)
		url = 'https://www.cardkingdom.com'

		search_by = search_by.lower().strip()
		name = name.lower().strip()

		if search_by == 'edition':
			url += '/mtg/' + name.replace(' ', '-')
		elif search_by == 'cardname':
			url += '/catalog/search?'
			url += 'search=header&'
			url += 'filter[name]=' + name.replace(' ', '+')

		self.start_urls = [url]

	def parse(self, response):
		for link in response.css('.productDetailTitle a'):
			yield response.follow(link, callback=self.parse_card)

		next_btn = response.css('.btn.btn-default.col-xs-4')[-1]
		if not 'disabled' in next_btn.attrib:
			link = next_btn.attrib['href']
			request = response.follow(link, callback=self.parse)

			yield request

	def parse_card(self, response):
		def extract_text(element):
			return element.css('::text').get().strip()

		info = {
			'name': extract_text(response.css('title')).split('|')[0].strip(),
			'price': extract_text(response.css('.stylePrice'))
		}

		trs = response.css('.table tr')
		for tr in trs:
			tds = tr.css('td')

			if len(tds) == 1:
				key = 'text'

				# if flavor text contains html tags, it wont be
				# retrieved completly.
				val = extract_text(tds[0])
			else:
				key = extract_text(tds[0])[:-1].lower()

				# For mana cost, info is in <img>'s, currently
				# parsing mana cost is not yet implemented
				if key == 'cast':
					val = ''
				else:
					val = extract_text(tds[1])

			info[key] = val

		yield info
