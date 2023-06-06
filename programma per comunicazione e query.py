## Importing Packges
import random
import influxdb_client, os, time
import pandas as pd
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "Danieli"
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "sensori"

# Define the write api
write_api = write_client.write_api(write_options=SYNCHRONOUS)

num = 0
dati = []
sensori = ["temperatura", "umidità", "pressione"]
posizione = ["dentro", "fuori"]

while num <= 20:
    dati.append({
        "sensore": random.choice(sensori),
        "location": random.choice(posizione),
        "num_sens": random.randint(0, 10),
        "val": random.randint(20, 500)
    })
    num += 1

for item in dati:
    point = (
        Point("census")
        .tag("sensore", item["sensore"])
        .field("location", item["location"])
        .field("num_sens", item["num_sens"])
        .field("val", item["val"])
    )
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(1)  # Separate points by 1 second

print("Complete. Return to the InfluxDB UI.")

'''
*******************************************************************************************************************************************************+
QUERY GET ALL
'''

from flightsql import FlightSQLClient

query = """SELECT * FROM 'census'"""

# Define the query client
query_client = FlightSQLClient(
  host = "eu-central-1-1.aws.cloud2.influxdata.com",
  token = os.environ.get("INFLUXDB_TOKEN"),
  metadata={"bucket-name": "sensori"})

# Execute the query
info = query_client.execute(query)
reader = query_client.do_get(info.endpoints[0].ticket)

# Convert to dataframe
data = reader.read_all()
df = data.to_pandas().sort_values(by="time")
print(df)



'''
*******************************************************************************************************************************************************+
'''


from flightsql import FlightSQLClient

query = "DELETE FROM census WHERE location >0"

# Define the query client
  org = "Danieli"
  url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
  bucket = "test"
  token = os.environ.get("INFLUXDB_TOKEN"),


client = InfluxDBClient(url=url, token=token)

# Esegui la query di eliminazione dei dati
query = 'DELETE FROM "census"'
client.query_api().query(org=org, query=query)

info = query_client.execute(query)
reader = query_client.do_get(info.endpoints[0].ticket)

# Convert to dataframe
data = reader.read_all()
print(data)




from influxdb_client import InfluxDBClient

# Definisci le informazioni di connessione a InfluxDB
org = "Danieli"
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
token = os.environ.get("INFLUXDB_TOKEN"),
bucket = "test"

# Crea un'istanza del client per la connessione a InfluxDB
client = InfluxDBClient(url=url, token=token)

# Esegui la query di eliminazione dei dati
query = 'DELETE FROM "census"'
client.query_api().query(org=org, query=query)

print("Dati cancellati correttamente.")
