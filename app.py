from flask import Flask, request, render_template
from model import predict_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        email_content = request.form['email']
        prediction = predict_email(email_content)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, render_template
# from encryptor import Encryptor
# import pickle

# app = Flask(__name__)
# encryptor = Encryptor()

# # Load the trained ML model
# model = pickle.load(open('model.pkl', 'rb'))
# vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get email content from the form
#     email_content = request.form['email']
    
#     # Encrypt the content
#     encrypted_content = encryptor.encrypt(email_content)
    
#     # Decrypt before processing
#     decrypted_content = encryptor.decrypt(encrypted_content)
    
#     # Vectorize the decrypted content
#     vectorized_content = vectorizer.transform([decrypted_content])
    
#     # Predict using the model
#     prediction = model.predict(vectorized_content)[0]
    
#     return render_template('result.html', prediction=prediction)

# if __name__ == '__main__':
#     app.run(debug=True)

