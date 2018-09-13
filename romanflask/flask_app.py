from flask import Flask, Response, request, jsonify
from roman_mapping import num2roman, roman2num

import logging


def create_app():
    logging.basicConfig(
        format='%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(levelname)s - %(message)s',
    )
    logger = logging.getLogger('roman')
    logger.setLevel(logging.DEBUG)
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'hello world'

    @app.route('/rom2num/<roman_string>')
    def rom2num(roman_string):
        logger.debug('------- Roman to Numeral -------')
        try:
            return jsonify({
                'roman': roman_string,
                'numeral': roman2num(roman_string)
            })
        except ValueError as e:
            return Response(str(e), 404)

    @app.route('/num2rom/<numeral>')
    def num2rom(numeral):
        logger.debug('------- Numeral to Roman -------')
        try:
            if numeral.isdigit():
                numeral = int(numeral)
                return jsonify({
                    'numeral': numeral,
                    'roman': num2roman(numeral)
                })
            raise ValueError('integer required')
        except ValueError as e:
            return Response(str(e), 404)

    return app


if __name__ == '__main__':
    create_app().run()
