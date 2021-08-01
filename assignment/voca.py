class Voca:
    def __init__(self, eng, kor, count=0):
        self.eng = eng
        self.kor = kor
        self.count = count

    def get_eng(self):
        return self.eng

    def get_kor(self):
        return self.kor

    def set_count(self, num):
        if self.count >= 0:
            return self.count + num

    def get_count(self):
        return int(self.count)

