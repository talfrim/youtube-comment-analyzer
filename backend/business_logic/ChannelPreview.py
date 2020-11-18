import json


class ChannelPreview:
    """class representing youtube channel preview"""

    def __init__(self, channel_id, title, description, thumbnail_url):
        self.id = channel_id
        self.title = title
        self.description = description
        self.thumbnailURL = thumbnail_url

    def get_dict(self):
        dictionary = vars(self)
        return dictionary

