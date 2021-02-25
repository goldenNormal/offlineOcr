from flask import Flask
from paddleocr import PaddleOCR, draw_ocr
import numpy as np
import base64
from io import BytesIO
from PIL import Image
from flask import  request
app = Flask(__name__)

base_path = "/code"
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

@app.route('/')
def hello():
    return  'hello'

def parseResult(result):
    res = []
    for line in result:
        positions = np.array(line[0],dtype='int').tolist()
        detail = { "content": line[1][0] , "accurate": str(line[1][1]),"positions": positions}
        res.append(detail)
    return res

def toPngStr(image):
    outBuffer = BytesIO()
    image.save(outBuffer, format="PNG")
    byte_data = outBuffer.getvalue()
    send_data = str(base64.b64encode(byte_data))
    send_str = 'data:image/png;base64,' + send_data[2:-1]
    return send_str

def drawImg(result,image):
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores,font_path="/code/doc/simfang.ttf")
    im_show = Image.fromarray(im_show)
    im_show.save(base_path+'/static/result.jpg')

    return toPngStr(im_show)


@app.route('/ocr',methods=["POST"])
def ocrController():

    file = request.files['image']
    print(file)
    img = Image.open(file)
    path = base_path+'/static/a.png'
    img.save(path)
    result = ocr.ocr(path, cls=True)

    res = { "code":200,"info":"ok","result": parseResult(result),"resultImg": drawImg(result,img)}
    return res




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)

