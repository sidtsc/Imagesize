from configparser import ConfigParser

def configprod(filename='database.ini', section='producao'):
	parser = ConfigParser()
	parser.read(filename)
	
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Sessão {0} não existe dentro {1} arquivo'.format(section, filename))

	return db
	
def configimg(filename='database.ini', section='imagens'):
	parser = ConfigParser()
	parser.read(filename)
	
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Sessão {0} não existe dentro {1} arquivo'.format(section, filename))

	return db