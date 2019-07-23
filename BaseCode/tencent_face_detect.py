import json
import requests


image_url = "http://mmbiz.qpic.cn/mmbiz_jpg/1plchJ7fW19nzGK3mibJNj4VcEF2aREu59ZmPfsGkTbmDlygcAR8iaj8EBCOLa7u7kZFVVAUNR8KS1FibRcu34qog/0"

request_url_format = "https://iai.tencentcloudapi.com/?Action=DetectFace&MaxFaceNum=1&MinFaceSize=40&Url={image_url}&NeedFaceAttributes=1&NeedQualityDetection=1&Version=2018-03-01"

request_url = request_url_format.format(image_url=image_url)

response = requests.get(request_url)
print(response.status_code)
print(json.loads(response.content))

