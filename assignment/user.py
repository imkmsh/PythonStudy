class User:
    def __init__(self, mail, pw, name, who):
        self.mail = mail
        self.pw = pw
        self.name = name
        self.who = who

    def get_name(self):
        return self.name

    def get_who(self):
        return self.who
