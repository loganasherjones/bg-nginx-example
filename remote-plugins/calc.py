import logging
from brewtils import system, command, parameter, Plugin

@system
class Calculator(object):

    @command
    @parameter(key='x', type=int)
    @parameter(key='y', type=int)
    def add(self, x, y):
        return x + y

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    c = Calculator()
    p = Plugin(
        c,
        bg_host='localhost',
        bg_port=80,
        name='calc',
        version='0.0.1.dev',
        username='admin',
        password='password',
        ssl_enabled=False,
        bg_url_prefix='/bg/'
    )
    p.run()
