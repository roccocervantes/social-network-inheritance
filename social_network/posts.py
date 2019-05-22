from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if not timestamp:
            timestamp = datetime.now()
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
#     def __init__(self, text, timestamp=None):
#         pass

    def __str__(self):
        return """@{first} {last}: "{content}"\n\t{time:%A, %b %d, %Y}""".format(first=self.user.first_name, last=self.user.last_name, content=self.text, time=self.timestamp)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return """@{first} {last}: "{content}"\n\t{image_url}\n\t{time:%A, %b %d, %Y}""".format(first=self.user.first_name, last=self.user.last_name, content=self.text, image_url=self.image_url, time=self.timestamp)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return """@{first} Checked In: "{content}"\n\t{lat}, {long}\n\t{time:%A, %b %d, %Y}""".format(first=self.user.first_name, content=self.text, lat=self.latitude, long=self.longitude, time=self.timestamp)
