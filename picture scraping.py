import requests, json
from urllib import request



BASE_URL = "http://api.vphotos.cn/vphotosgallery/wechat/album/getPhotoListByWeChatId"
data = {
    "weChatId": "B9C4A3934686B47056F2401472D59BD0",
    "photoId": "585fb1e8e4b05f2d6a299555",
    "pageSize": 455,
    "defaultPhotoSizeType": 8,
    "uId": "15305807967850474",
    "sort": "desc"
}
res = json.loads(requests.post(BASE_URL, data=data).text)
list = res['data']['photos']
id = 1
for photo in list:
    url = photo['smallUrl']
    name = photo['photoName']
    request.urlretrieve(url, f'D:\\beida\{name}.jpg')
    id += 1
    print(f"id:{id}")


