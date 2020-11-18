import json

from service import channels
from flask import Flask, jsonify, request
app = Flask(__name__)


''' ALIVE TEST '''
@app.route('/alive')
def alive():
    return "I'm alive"


''' CHANNELS '''
@app.route('/channels/searchChannels', methods=['GET'])
def getChannels():
    q = request.args.get('q')
    if q is not None:
        res = channels.search_channels(q)
        return res
    else:
        return "server error", 500


''' VIDEOS '''



if __name__ == "__main__":
    app.run()


