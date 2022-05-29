from flask_mail import *
from flask import *
from segredos import *

app = Flask(__name__)
app.secret_key = 'thicode'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
        user = request.form.get("name"),
        emaill = request.form.get("email"),
        subject = request.form.get("subject"),
        message = request.form.get("message")

        msg = Message(
            subject=f'{user[0]}',
            sender=app.config.get("MAIL_USERNAME"),
            recipients=['mateusdosummerblog@gmail.com'],
body=f'''
𝗔𝘀𝘀𝘂𝗻𝘁𝗼: {subject[0]}

𝗘𝗺𝗮𝗶𝗹: {emaill[0]} 
            
𝗠𝗲𝗻𝘀𝘀𝗮𝗴𝗲𝗺: {message}
        
''')

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
        return redirect('/')


@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


if __name__ == '__main__':
    app.run(debug=True)
