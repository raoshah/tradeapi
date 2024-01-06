from flask import Flask , render_template

import pyotp, json, http.client, os, threading, time


app = Flask(__name__)
app.secret_key = "srr"


counter = 0
def count():
    global counter
    while True:
        counter = counter + 1
        time.sleep(1)
        print(counter)



@app.route('/')
def index():
    count_thread = threading.Thread(target=count)
    count_thread.start()
    return str(counter)





if __name__ == '__main__':
    app.run(debug=True) 