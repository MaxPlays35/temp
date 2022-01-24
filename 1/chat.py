import datetime


class Chat:
    def __init__(self) -> None:
        self.messages = []
        self.users = dict()
    
    def get_messages(self):
        return self.messages[-20:]
    
    def login(self, ip_addr, name):
        self.users[ip_addr] = name
    
    def add_message(self, ip_addr, message):
        name = self.users.get(ip_addr, "unknown")
        ts = datetime.datetime.now()

        if len(self.messages) > 30:
            self.messages = self.messages[-30:]

        self.messages.append({
            "name": name,
            "ts": ts,
            "message": message
        })
