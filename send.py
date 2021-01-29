import grequests
import threading
import time
import pika

#opening the connection to RabbitMQ
connection = pika.BlockingConnection( pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

#declaring queue with name 'pipeline'
channel.queue_declare(queue='pipeline')


urls = [
    'https://www.thecocktaildb.com/api/json/v1/1/random.php',
    'https://randomuser.me/api/',
]

def get_data(x):
	rs = (grequests.get(u) for u in urls)
	responses = grequests.map(rs)

	for r in responses:		
		channel.basic_publish(exchange='', routing_key='pipeline', body=r.text)
		print(" [x] Sent " + str(x))


for i in range(15): #creating 15 threads
	threading.Thread(target = get_data, args = (i+1,)).start()
	
	#giving sleep time 5 -> to create threads every 5 seconds
	time.sleep(5) 

connection.close()
print(" [x] connetion closed")