from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.fooddata
collection = db.line
datas = [
    {
        "type": "high",
        "courseImg": "https://s1.cdn.xiangha.com/caipu/201205/1621/162148329694.jpg/MjgweDIyMA.webp"
    },
    {
        "type": "lazy",
        "courseImg" : "https://s1.cdn.xiangha.com/caipu/201604/1611/161104267121.jpg/MjUweDI1MA.webp"
    }
]
for data in datas:
    collection.insert_one(data)