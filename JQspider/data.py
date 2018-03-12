from pymongo import MongoClient

class SpiderData(object):
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def write_datas(self):
        client = MongoClient('localhost', 27017)
        db = client.fooddata
        collection = db.foods
        for data in self.datas:
            collection.insert_one(data)