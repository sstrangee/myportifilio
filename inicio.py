from flask import *
import smtplib
from email.message import EmailMessage
from segredos import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():
    user = request.form["name"],
    emaill = request.form["email"],
    subject = request.form["subject"],
    message = request.form["message"],
    EMAIL_ADDRESS = email
    EMAIL_PASSWORD = senha

    msg = EmailMessage()
    msg['subject'] = f"{user[0]}"
    msg['from'] = 'ssseer'
    msg['to'] = 'mateusdosummerblog@gmail.com'
    msg.set_content(f'''
    𝗔𝘀𝘀𝘂𝗻𝘁𝗼: {subject[0]}
    
𝗠𝗲𝗻𝘀𝘀𝗮𝗴𝗲𝗺: {message[0]}
    
    𝗘𝗺𝗮𝗶𝗹: {emaill[0]} ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    return redirect('/')


@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


if __name__ == '__main__':
    app.run(debug=True)
