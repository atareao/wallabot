#!/usr/bin/env python3
from flask import Flask, jsonify, make_response, request
from telegramapi import TelegramApi
from wallabagapi import WallabagApi
import time
import os
import sys
import re


app = Flask(__name__)

telegramApi = TelegramApi(os.environ['TELEGRAM_API_TOKEN'])
wallabagApi = WallabagApi(os.environ['WALLABAG_BASE_URI'], os.environ['CLIENT_ID'],
                          os.environ['CLIENT_SECRET'], os.environ['USERNAME'],
                          os.environ['PASSWORD'])

def logger(message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    sys.stdout.write('{} | {}\n'.format(timestamp, message))


@app.route('/status', methods=['GET'])
def get_status():
    return 'Up and running', 201

@app.route('/webhook/<webhook>', methods=['GET', 'POST'])
def get_webhook(webhook):
    logger(webhook)
    if os.environ['WEBHOOK'] != webhook:
        return 'KO', 404
    try:
        if request.method == 'GET' or not request.json:
            return 'OK', 200
    except Exception:
        return 'OK', 200
    payload = request.json
    if 'message' in payload and 'text' in payload['message']:
        chat_id = payload['message']['chat']['id']
        test_str = payload['message']['text']
        logger("Text to process: {}".format(test_str))
        regex = r"^(https?://[^\s/$.?#].[^\s]*)$"
        matches = re.search(regex, test_str, re.IGNORECASE)
        if matches:
            url_to_wallabag = matches.group(1)
            logger("Url found: {}".format(url_to_wallabag))
            response = wallabagApi.post(url_to_wallabag)
            if response:
                msg = "The url {} was added to Wallabag as <strong>{}</strong>".format(
                        url_to_wallabag, response['title'])
                logger("Url {} added".format(url_to_wallabag))
            else:
                msg = "Can't add {} to Wallabag".format(url_to_wallabag)
                logger("Url {} NOT added".format(url_to_wallabag))
            telegramApi.send_message(chat_id, msg)
    return 'OK', 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
