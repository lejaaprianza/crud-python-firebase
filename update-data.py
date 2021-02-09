from firebase import firebase


firebase = firebase.FirebaseApplication(
    'https://fir-crud-python-default-rtdb.firebaseio.com/', None)

result = firebase.put('/Identitas/-MT5qWTa6BG4q84Ow3zr', 'Umur', '17')
