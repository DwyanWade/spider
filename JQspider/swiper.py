from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.fooddata
collection = db.swiperimg
datas = [
    {
        "courseId" : 106,
        "courseImg" : "https://s1.cdn.xiangha.com/caipu/201801/1812/181225526405.jpg/NjAwX2MxXzQwMA"
    },
    {
        "courseId" : 107,
        "courseImg" : "https://s1.cdn.xiangha.com/caipu/201801/1722/17220249430.jpg/NjAwX2MxXzQwMA"
    },
    {
        "courseId" : 150,
        "courseImg" : "https://s3.cdn.xiangha.com/caipu/201801/1822/182239438673.jpg/NjAwX2MxXzQwMA"
    },
    {
        "courseId" : 159,
        "courseImg" : "https://s3.cdn.xiangha.com/caipu/201601/2913/291344599467.jpg/NjAwX2MxXzQwMA"
    }
]
for data in datas:
    collection.insert_one(data)