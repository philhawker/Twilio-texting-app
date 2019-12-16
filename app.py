# THIS IS ALL BOILERPLATE CODE

from flask import Flask, request, render_template
from twilio.rest import Client
import config

app = Flask(__name__)
# BOILERPLATE ENDS HERE

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send_sms', methods=['POST'])
def send_sms():
    phone_number = None
    if request.method == 'POST':
        phone_number = request.form['phone']
        message = request.form['message']
        account_sid = config.ACCOUNT_SID
        auth_token = config.AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body= f"{message}",
                            from_='+13343105939',
                            to=f"+{phone_number}"
                        )

        print(message.sid)
        return render_template('message_sent.html')
    return home()

# PART OF BOILERPLATE
if __name__ == "__main__":
    app.run(debug=True)
