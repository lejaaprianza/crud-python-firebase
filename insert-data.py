from firebase import firebase


firebase = firebase.FirebaseApplication(
    'https://fir-crud-python-default-rtdb.firebaseio.com/', None)
data = {'Nama': 'Leja Aprianza',
        'Status': 'Mahasiswa',
        'Umur': 10
        }
result = firebase.post('/Identitas/', data)
print(result)
