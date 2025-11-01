

users = [
    
    {
        '_id':'ObjectID',
        'username':'UserX',
        'role': 'user',
        'password': 'fsxffeqfacx',
        'createdAt':'ISODate'
    },

    {
        '_id':'ObjectID',
        'username':'UserY',
        'role': 'admin',
        'password': '524tgdasg',
        'createdAt':'ISODate'
    },

    {
        '_id':'ObjectID',
        'username':'UserZ',
        'role': 'user',
        'password': '35q25245q',
        'createdAt':'ISODate'
    }

]

devices = [
    {
        '_id': 'ObjectID',
        'device': 'Device1',
        'createdAt':'ISODate'
    },

    {
        '_id': 'ObjectID',
        'device': 'Device2',
        'createdAt':'ISODate'
    },

    {
        '_id': 'ObjectID',
        'device': 'Device3',
        'createdAt':'ISODate'
    },

]

chamadas = [
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device1',
        'Local': '<local_chamada>',
        'Data': 'ISODate'
    },

    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device2',
        'Local': '<local_chamada>',
        'Data': 'ISODate'
    },
    
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device3',
        'Local': '<local_chamada>',
        'Data': 'ISODate'
    },
]

status_chamadas =[
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device1',
        'Local': '<local_chamada>',
        'status': 'emergencia',
        'updateAt': 'ISODate'
    },

    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device2',
        'Local': '<local_chamada>',
        'status': 'oscioso',
        'updateAt': 'ISODate'
    },
    
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device3',
        'Local': '<local_chamada>',
        'status': 'emergencia',
        'updateAt': 'ISODate'
    }
]

status_chamadas_emergencia = [
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device1',
        'Local': '<local_chamada>',
        'status': 'emergencia',
        'updateAt': 'ISODate'
    },

    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device2',
        'Local': '<local_chamada>',
        'status': 'emergencia',
        'Data': 'ISODate'
    },
    
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device3',
        'Local': '<local_chamada>',
        'status': 'emergencia',
        'Data': 'ISODate'
    }
    
]


status_chamadas_oscioso = [
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device1',
        'Local': '<local_chamada>',
        'status': 'oscioso',
        'Data': 'ISODate'
    },

    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device2',
        'Local': '<local_chamada>',
        'status': 'oscioso',
        'Data': 'ISODate'
    },
    
    {
        '_id': 'ObjectID',
        'dispositivo_id': 'Device3',
        'Local': '<local_chamada>',
        'status': 'oscioso',
        'Data': 'ISODate'
    }
    
]