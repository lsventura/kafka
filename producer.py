import pandas  as pd
import ssl
from kafka import KafkaProducer
from kafka import KafkaConsumer
from time import sleep
from json import dumps
from kafka import KafkaProducer


# ssl._create_default_https_context = ssl._create_unverified_context

# url = 'https://dados.anvisa.gov.br/dados/TA_PRECO_MEDICAMENTO.csv' #dados publicos
# df = pd.read_csv(url,  sep = ',')
# df.head()

# Produtor
# def envia_mensagem(msg):
#     producer = KafkaProducer(bootstrap_servers='localhost:9092')
#     try:
#         producer.send('teste_leo', b" enviando ")
#         result = "deu bom"
#     except:
#         result = "Deu ruim: "

#     return result

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)

# if __name__ == '__main__':
#     envia_mensagem("testando 123")   


# Consumidor
# consumer = KafkaConsumer('sample')
# for message in consumer:
#     print (message) 