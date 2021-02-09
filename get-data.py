from firebase import firebase


firebase = firebase.FirebaseApplication(
    'https://fir-crud-python-default-rtdb.firebaseio.com/', None)

result = firebase.get('/Identitas/', '')
print(result)
