import json
import paho.mqtt.client as mqtt

BROKER_HOST = 'localhost'
BROKER_PORT = 1883
id_test = 'pub_test'
pass_test = '123'

def publish_message(topic: str, payload: dict):
    """Publica uma mensagem MQTT no tópico especificado."""
    client = mqtt.Client(client_id=id_test)
    client.username_pw_set(id_test, pass_test)
    client.connect(BROKER_HOST, BROKER_PORT)
    client.publish(topic, json.dumps(payload))
    client.disconnect()
    print(f"Mensagem publicada em '{topic}': {payload}")

def pub_posto_enfermaria_de_enfermaria(dispositivo_id: str, estado: str, mensagem: str, room_number: str, local:str, comando: str):
    """Publica um evento vindo da enfermaria."""
    topic = f'dispositivos/posto_enfermaria/{dispositivo_id}'
    payload = {
        'id': dispositivo_id,
        'estado': estado,
        'mensagem': mensagem,
        'room_number': room_number,
        'local': local,
        'comando': comando
    }
    publish_message(topic, payload)

def pub_enfermaria_de_posto_enfermaria(dispositivo_id: str, estado: str, mensagem: str, room_number: str, local:str, comando: str):
    """Publica um evento vindo do posto de enfermaria no tópico local."""
    topic = f'dispositivos/enfermaria/{dispositivo_id}'
    payload = {
        'id': dispositivo_id,
        'estado': estado,
        'mensagem': mensagem,
        'room_number': room_number,
        'local': local,
        'comando': comando
    }
    publish_message(topic, payload)

# ====== EXEMPLOS DE USO ======
pub_posto_enfermaria_de_enfermaria(

        dispositivo_id='enfermaria2',
        estado='emergencia',
        mensagem='ligar LED',
        room_number='1',
        local='enfermaria',
        comando='ligar'
        
)

'''
pub_enfermaria_de_posto_enfermaria(
        dispositivo_id='enfermaria10',
        estado='oscioso',
        mensagem='desligar LED',
        room_number='10',
        local='enfermaria',
        comando='desligar'
)
'''
