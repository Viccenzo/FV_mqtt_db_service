
# FV MQTT DB Service

## Descrição Geral
O FV MQTT DB Service é um serviço que permite a inserção assíncrona de dados em um banco de dados utilizando o protocolo MQTT. Ele inclui funções para inicializar o serviço, conectar-se ao servidor MQTT e enviar dataframes pandas para o banco de dados.

## Requisitos
- Python 3.x
- pandas
- paho-mqtt

## Instalação
Primeiro, instale as dependências necessárias utilizando o `pip`:
```bash
pip install -r requirements.txt
```

## Arquitetura do Projeto
- `main.py`: Arquivo principal que demonstra como utilizar o serviço `mqtt_db_service`.
- `mqtt_db_service/mqtt_db_service.py`: Implementação principal do serviço.

## Uso

### Inicialização do Serviço
A função `initDBService` inicializa o serviço MQTT e configura os clientes MQTT.
```python
import time

# Callback assíncrono para inserção no banco de dados
def callback(client, userdata, msg):
    print("Message on topic: " + msg.topic + " was: " + msg.payload.decode())

# Inicializa o serviço
service.initDBService(callback, user="viccenzo", server1="8.8.8.8", server2="8.8.8.8")
```

### Exemplo de DataFrame
A função `dataframeExample` cria um exemplo de dataframe para fins de teste.
```python
# Cria um dataframe de teste
df = service.dataframeExample()
print("IMPORTANT! YOU NEED TO SPECIFY A <TIMESTAMP> COLUMN")
print(df)
```

### Envio de Dados
A função `sendDF` envia um dataframe pandas para o banco de dados via MQTT.
```python
# Envia o dataframe junto com o nome do usuário e o nome da tabela que deseja usar
print(service.sendDF(df, table="teste5"))
```

### Loop Principal
Mantém o script em execução para ouvir as mensagens MQTT.
```python
while True:
    pass
```

## Funções Detalhadas

### `dataframeExample()`
Cria um exemplo de dataframe pandas com colunas `TIMESTAMP`, `calories` e `duration`.

**Retorno**
- `pd.DataFrame`: DataFrame de exemplo.

### `initDBService(callback, user, server1, server2)`
Inicializa o serviço MQTT com dois servidores MQTT e um callback para mensagens.

**Parâmetros**
- `callback (function)`: Função de callback para mensagens MQTT.
- `user (str)`: Nome do usuário.
- `server1 (str)`: Endereço do primeiro servidor MQTT.
- `server2 (str)`: Endereço do segundo servidor MQTT.

**Retorno**
- Null

### `sendDF(df, table)`
Envia um dataframe pandas para o banco de dados via MQTT.

**Parâmetros**
- `df (pd.DataFrame)`: DataFrame a ser enviado.
- `table (str)`: Nome da tabela do banco de dados.

**Retorno**
- `str`: Mensagem de sucesso ou erro no uso da biblioteca.
