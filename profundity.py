#!/usr/bin/env python

# What an incredibly stupid application.
# I realize that it's released under the MIT License.
# But, seriously.  Who cares?

import datetime
import json
import logging
import os
import sys
import BaseHTTPServer as http

def port_from_env():
    return int(os.getenv('PROFOUND_PORT', '8080'))

def name_from_env():
    return os.getenv('PROFOUND_NAME', 'Profundity (Xtream!)')

def configure_logger():
    logging.basicConfig(format='%(asctime)s.%(msecs)03d #%(process)d - %(levelname)s %(name)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level='INFO')
    return logging.getLogger()

def run(port, name, logger):
    logger.info('xtream profundity server starting.')
    server = http.HTTPServer(('', port), Profundity.named_handler(name))
    logging.info('serving "%s" on port %d', name, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info('Received Ctrl-C; exiting.')
    logger.info('Done.')

class Profundity(http.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('X-Service-Name', self.NAME)
        self.end_headers()
        response = json.dumps({
                'service': self.NAME,
                'time': datetime.datetime.utcnow().strftime('%Y-%m%-dT%H:%M:%SZ'),
                'client': ':'.join(str(f) for f in self.client_address),
                'request-path': self.path,
            })
        logging.getLogger().info('Responding: %s', response)
        self.wfile.write(response)

    @classmethod
    def named_handler(cls, name):
        class ProfundityHandler(cls):
            NAME = name
        return ProfundityHandler

def show_usage():
    print >> sys.stderr, "Usage: %s\n\nEnvironment variables:" % __file__, \
                         "\n  PROFOUND_PORT - port to listen on (8080)", \
                         "\n  PROFOUND_NAME - name to use for identifying this excellent 'service' ('Profundity (Xtream!)')", \
                         "\n"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if '-h' in sys.argv[1:] or '--help' in sys.argv[1:]:
            show_usage()
            exit()
        else:
            show_usage()
            exit(1)
    run(port_from_env(), name_from_env(), configure_logger())

