import status

def help():
	return "oi ou olá -> retorna uma saudação\ninfo -> retorna informações de compra e venda\ncontato -> retorna informações de contato"

def sample_responses(input_text):
	user_message = str(input_text).lower()
	
	if user_message in ("oi", "ola", "olá"):
		return "E ai, blz?"

	elif user_message == "contato":
		return "http://alexsetta.com/ \n            Acesse! ☝️"

	elif user_message in ("info", "inf", "rsi"):
		return status.get()

	return "Comando inválido. Tente: /help?"
	