#TODO should we use async await here?


import requests

from business_logic.ChannelPreview import ChannelPreview

api_key = "AIzaSyDP7adS-CnabpH1uTSDs8jjldgOVQq2mSQ"
base_url = "https://youtube.googleapis.com/youtube/v3/"

""" channels """
# This function returns a list of up to 5 top channel ids according to the name entered
def get_channels_ids_by_name(name):
    req_url = base_url + "search?part=snippet&maxResults=5&q=" + name +\
              "&type=channel&fields=items%2Fsnippet%2FchannelId&key=" + api_key
    res = requests.get(req_url)
    if int(res.status_code) == 200:
        return extract_ids_from_ids_results(res.json())


# This methods returns ChannelPreview object according to the id entered
def get_channel_preview_by_id(channel_id):
    req_url = base_url + "channels?part=snippet&id=" \
              + channel_id + "&key=" + api_key  # only snippet, add statistics if we want (for subscribers, etc)
    res = requests.get(req_url)
    if int(res.status_code) == 200:
        result_json = res.json()
        channel_data = result_json["items"][0]
        return ChannelPreview(channel_data["id"], channel_data["snippet"]["title"],
                              channel_data["snippet"]["description"], channel_data["snippet"]["thumbnails"]["medium"]["url"])


def extract_ids_from_ids_results(results_json):
    result_list = []
    for obj in results_json["items"]:
        result_list.append(obj["snippet"]["channelId"])
    return result_list

