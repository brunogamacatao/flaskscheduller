import time
import atexit

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

tempo_para_explodir = 10

def reinicia_temporizador():
    global tempo_para_explodir
    tempo_para_explodir = 10

def job_function():
    global tempo_para_explodir
    print(str(tempo_para_explodir) + ' tique-taque')
    tempo_para_explodir -= 1
    if tempo_para_explodir <= 0:
        print('Boom !')
        reinicia_temporizador()

scheduler = BackgroundScheduler()
scheduler.add_job(job_function, 'interval', seconds=1)
scheduler.start()

app = Flask(__name__)

@app.route('/')
def hello():
    global tempo_para_explodir
    msg = 'Evitei a explosão faltando ' + str(tempo_para_explodir) + ' segundos'
    reinicia_temporizador()
    return msg

if __name__ == '__main__':
    app.run()
