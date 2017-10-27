import time
import pymysql


hostname = 'localhost'
username = 'root'
password = ''
database = 'whatsapptmx'
myConnection =""

def doQuery( myQuery) :
	global myConnection
	myConnection =pymysql.connect( host=hostname, user=username, passwd=password, db=database )	#Crear la conexión con la BD
	cur = myConnection.cursor()
	cur.execute( myQuery )
	result=cur.fetchall()
	return result

"""def verificaConexionOperador(listaIdOperadores):
	for idop in listaIdOperadores:
		hoy = time.strftime("%H:%M")
		fecha=doQuery("SELECT fechaContacto FROM mensajes_activos ma INNER JOIN conversaciones conv WHERE ma.idConversacion = conv.idConv AND conv.idOperador='"+idop+"'")
"""



hoy = time.strftime("%H:%M")

hrsys=int(time.strftime("%H"))
mnsys=int(time.strftime("%M"))

mnsys=mnsys+5

future = str(hrsys)+":"+str(mnsys)

print("current + 5 mins->"+future)

celular="Ya TODOS Juntos"

consulta = doQuery("SELECT fechaInsert FROM clientes_por_atender WHERE numCelular='"+celular+"'") [0][0] ;
hrbd = int(consulta.strftime("%H"))
mnbd = int(consulta.strftime("%M"))

hora=consulta.strftime("%H:%M")

print(hora)

if( hrbd <= hrsys):
	print("Parece estar vivo")
	if(mnsys >= mnbd):
		print("Se necesita saber si está vivo")
	else:
		print("Está vivo")