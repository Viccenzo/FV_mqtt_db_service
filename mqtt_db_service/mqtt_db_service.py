import pandas as pd
import paho.mqtt.client as mqtt

client1 = mqtt.Client()
client2 = mqtt.Client()
topicUser = ""

def dataframeExample():
    data = {
        "TIMESTAMP": ["2024-07-30 20:01:48","2024-07-30 20:01:44","2024-07-30 20:01:49"],
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    return pd.DataFrame(data)

def on_connect(client, userdata, flags, rc):
    #print(f"Conectado com o código de resultado {rc}")
    client.subscribe(f'message/{userdata}/#')  # Subscrição ao tópico passado via userdata

def initDBService(callback,user,server1,server2):
    global client1
    global client2
    global topicUser
    
    topicUser = user

    #client1
    client1 = mqtt.Client(userdata=user)
    mqtt_broker = server1 #"58296fae6ca74b90bda9fc67e3646310.s1.eu.hivemq.cloud"
    mqtt_port = 1883  #8883
    client1.connect(mqtt_broker, mqtt_port)
    client1.on_message = callback
    client1.on_connect = on_connect
    client1.loop_start()
    
    #client2
    #mqtt_broker = server2 #"58296fae6ca74b90bda9fc67e3646310.s1.eu.hivemq.cloud"
    #mqtt_port = 1883  #8883
    #client2.connect(mqtt_broker, mqtt_port)
    #client2.on_message = callback
    #client2.on_connect = on_connect
    #client2.loop_start()

def sendDF(df,table):
    global client1
    global client2
    global topicUser

    user = topicUser

    if not isinstance(df,pd.DataFrame):
        return ("pandas dataframe is not correct")
    if not user:
        return ("missing user argument")
    if not isinstance(user, str):
        return ("user should be of type string")
    if not table:
        return ("missing user argument")
    if not isinstance(table, str):
        return ("user should be of type string")

    try:    
        client1.publish(f'DB_INSERT/{user}/{table}', df.to_json(), qos=1)
    except:
        client2.publish(f'DB_INSERT/{user}/{table}', df.to_json(), qos=1)
        return "Your db insertion was send to backend through secondary gateway. please inform service provider"
    return "Your db insertion was send to backend"
