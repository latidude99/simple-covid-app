class Comment:

    def __init__(self, time, user, url, text, registered, blocked):
        self.time = time
        self.user = user
        self.url = url
        self.text = text
        self.registered = registered
        self.blocked = blocked

    def __str__(self):
        return str(self.time) + \
               " " + self.user + \
               " " + str(self.url) + \
               " " + str(self.text) + \
               " " + str(self.registered) + \
               " " + str(self.blocked)
