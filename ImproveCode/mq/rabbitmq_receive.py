import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print('[x] Receive %s' % body)


channel.basic_consume('hello',
                      callback
                      )
print("[*] Waiting for message, To exit press CTRL+C")
channel.start_consuming()
