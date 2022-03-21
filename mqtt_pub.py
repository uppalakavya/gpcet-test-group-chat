import paho.mqtt.client as mqtt
pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)
print('Broker Connected ')

for i in range(5):
    pub_client.publish('gpcet/ai','Kavya here...')
 
