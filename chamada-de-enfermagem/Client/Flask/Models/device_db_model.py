from MongoDB.MongoDBConnection import MongoDBConnection


'''
Classe para crud com devices e inserir novos dispositivos 
'''
class DeviceDBModel():

    def __init__(self, db:MongoDBConnection):
        self.db = db

    def find_by_device(self, device:str):
        return self.db.check_if_document_exists('devices', 'device', device)
    
    def find_device_by_id(self, document_id:str) -> bool:
        return self.db.check_if_document_exists_by_id('devices', document_id)
    
    def insert_device(self, device_data:dict):
        return self.db.insert_document_collection('devices', device_data)
    
    def update_device(self, document_id:str, documents_with_updates:dict):   
        return self.db.update_document_by_id('devices', document_id, documents_with_updates)


    def delete_device_by_id(self, document_id:str):
        return self.db.delete_document_by_id('devices', document_id)
    
    def return_count_all_devices(self):
        return self.db.count_all_documents_on_collection('devices')

    def return_all_devices(self):
        return self.db.list_all_documents_from_collection('devices')