# import argparse
import optparse

from elastichq import create_app
from elastichq.globals import socketio

default_host = '0.0.0.0'
default_port = 5000
default_debug = False

application = create_app()

if __name__ == '__main__':
    # Set up the command-line options
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug", default=default_debug,
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    socketio.run(application, host=options.host, port=options.port, debug=options.debug)

