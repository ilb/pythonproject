import gunicorn
from bottle import Bottle

heartbeat = Bottle()


@heartbeat.get()
def heartbeat(req, res):
    heartbeat_answer = "200 OK <br/> " \
                       f"gunicorn version: {gunicorn.__version__} <br/> "
    return heartbeat_answer
