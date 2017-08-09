import psycopg2
from config import configprod
from config import configimg

def connect():
	"""Connect to the PostgreSQL database server """
	conn = None
	
	try:
	
		#read connection parameters#
		params = configprod()

		#connect to the PostgreSQL server
		print('Conectando no Postgresql Database...')
		conn = psycopg2.connect(**params)

		# Criando o cursor
		cur = conn.cursor()
		
		#Executar o comando
		print('Postgresql database versão:')
		cur.execute('Select cdpessoa from ecdtpessoa order by cdpessoa desc limit 10')
		row = cur.fetchone()
	  
		while(row is not None):
		 ##Conectar no bd de imagem
		 paramsimg = configimg()
		 conimg = psycopg2.connect(**paramsimg)
		 curimg = conimg.cursor()
		 print (row)
		 curimg.execute('select * from ecdtpessoaimagem order by cdpessoa desc limit 1')
		 rowimg = curimg.fetchone()
		 print(rowimg)
		 #print(row)
		 row = cur.fetchone()
	  
		#fechando a comunicação com o Postgresql
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
	   print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Conexão com o Postgresql fechada')

if __name__ == '__main__':
	connect()