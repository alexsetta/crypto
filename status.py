from bs4 import BeautifulSoup
import requests
import datetime

def get():
	url = "https://br.investing.com/crypto/bitcoin/btc-brl-technical"

	page = requests.get(url, headers={'User-Agent': 'XYZ/3.0'}).content
	soup = BeautifulSoup(page, "html.parser")

	results = soup(id="curr_table", class_="genTbl closedTbl technicalIndicatorsTbl smallTbl float_lang_base_1")
	table = results[0]

	tmp = table.find("td", class_="right").get_text()
	tmp = tmp.replace(",", ".")
	rsival = int(float(tmp))
	rows = table.findAll("span")
	rsi = rows[0].get_text()
	rows = rows[len(rows)-7:]

	compra = int(rows[1].get_text())
	venda = int(rows[3].get_text())
	neutro = int(rows[5].get_text())
	resumo = rows[6].get_text()

	total = compra+venda+neutro
	if resumo == "Compra":
		divisor = compra
	elif resumo == "Venda":
		divisor = venda
	else:
		divisor = neutro

	indice = divisor*100/total

	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
	print(now)
	txt = f"{now}\n"
	txt += f"Compra: {int(compra/total*100)}%\n" 
	txt += f"Venda: {int(venda/total*100)}%\n" 
	txt += f"Neutro: {int(neutro/total*100)}% \n" 
	txt += f"Resumo: {resumo} \n"
	txt += f"RSI: {rsi} ({rsival}%)\n"
	if rsival <= 30:
		txt += "AÇÃO: COMPRAR\n"
	elif rsival >= 70:
		txt += "AÇÃO: VENDER\n"
	return txt
		
		
