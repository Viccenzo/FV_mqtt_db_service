import mqtt_db_service as service
import pandas as pd
import time

# Asynchronous DB insert callback
# Here is where you will receive messages back from the server if something happens
def callback(client, userdata, msg):
    print("Message on topic: " + msg.topic + " was: " + msg.payload.decode())

# Init Service
# This command will start the service and will assign the callback function
service.initDBService(callback, user="gonzaga", server1="8.8.8.8", server2="8.8.8.8")

# Create test dataframe
# This is just for testing purposes and to show how the code works. Create your own dataframe to test. Don't forget to include a "TIMESTAMP" column
df = pd.DataFrame()
df = service.dataframeExample()
print("IMPORTANT! YOU NEED TO SPECIFY A <TIMESTAMP> COLUMN")
print(df)

time.sleep(1)

# Send data function
# Send your dataframe along with your name and the table name that you would like to use
print(service.sendDF(df, table="teste"))

while True:
    pass
