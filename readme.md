# 启动命令
当前目录下
```
docker build -t <镜像的名字> .
docker run -d -p <本机的端口>:5000 --name <容器的名字> <镜像的名字>
```

例如
```
docker build -t myocr .
docker run -itd --rm -p 5000:5000 --name ocr myocr
```

# 接口调用
## 测试启动
```http request
 http://localhost:5000/
测试是否服务器已经启动
返回值为 'hello'
```

## ocr接口
```angular2
http://localhost:5000/ocr
ocr识别接口，方法为POST，contentType 为 multipart/form-data
```
请求参数

|   key  |  value |
|  ----  | ----  |
|   file  |  图片流 |

返回参数

|   key  |  value |
|  ----  | ----  |
|   result  |  文字识别结果，包括识别内容，准确度，位置 |
|   resultImg  |  提取文字后新图片的png流 |


