# image 경로에 대한 http 요청을 처리할 함수를 지정.
# user가 웹 브라우저에서 /image url에 접근하면 아래에 정의된 image()함수가 실행됨.
@app.route('/image')

# 이 함수는 사용자가 /image 경로에 접근했을 때 실행됩니다.
def image():
    # HTTP 요청 헤더에서 Referer 정보를 가져옵니다.
    referer = request.headers.get('Referer')
    # referer가 존재하고, 그 값에 'yourdomain.com'이 포함되어 있는지를 확인합니다. (외부사이트에서의 접근을 차단할때 사용함.)
    if referer and 'your-domain.com' in referer:
# 사용자가 허용된 도메인에서 요청한 경우,
# 서버는 send_file 함수를 사용하여 지정된 이미지 파일(path/to/image.jpg)을 클라이언트에게 반환합니다. (이때 실제 이미지가 브라우저에서 표시됨.)
        return send_file('path/to/image.jpg')
    # 이 코드는 클라이언트에게 요청이 허용되지 않았음을 알립니다. (허용되지 않은 도메인 요청이 오면 접근을 차단 함.)
    return 'Access Denied', 403

# 학원 컴퓨터에서는 연계 파일을 cmd로 다운 받지 않아서 밥먹고 다운 받아야 할듯?

# -url을 사용할때의 방식-
# import requests
# from flask import Flask, send_file, abort
# from io import BytesIO

# app = Flask(__name__)

# @app.route('/url')
# def image():
#     referer = request.headers.get('Referer')
#     if referer and 'yourdomain.com' in referer:
#         image_url = 'https://example.com/path/to/image.jpg'  # 외부 이미지 URL
#         response = requests.get(image_url)
        
#         if response.status_code == 200:
#             return send_file(BytesIO(response.content), mimetype='image/jpeg')
#         else:
#             return 'Image not found', 404
            
#     return 'Access Denied', 403

