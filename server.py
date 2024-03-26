from flask import Flask, Blueprint,request
from Common.CommonResult import CommonResult
from flask_cors import CORS
import jwt
import datetime
import random

app = Flask(__name__)   
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app,origins="*",allow_headers="*")
api = Blueprint('api', __name__, url_prefix='/api')

# @api.before_request
# def before_request_func():
#     # 指定不需要验证Token的路由列表
#     if request.endpoint in ['login', ]:
#         return  # 对于公开路由，不执行任何操作，直接返回
#     token = request.headers.get('Authorization').split(" ")[1] if request.headers.get('Authorization') else None
#     if not token:
#         return CommonResult.fail({'message': 'Token is missing!'})
#     try:
#         # 解码JWT Token
#         jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#     except jwt.ExpiredSignatureError:
#         return CommonResult.fail({'message': 'Token has expired!'})
#     except jwt.InvalidTokenError:
#         return CommonResult.fail({'message': 'Invalid token!'})


@api.route('/login',methods=['GET'])
def login():
    users = {'yxy': '123'}
    name = request.args.get('name')
    password = request.args.get('password')
    token = ''
    if name in users and users[name] == password:
        # 如果用户验证成功，生成JWT
        token = jwt.encode({
            'user': name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')

    ret = {
        'id': '1',
        'name':'yxy',
        'password':'123',
        'token':token
    }
    return CommonResult.success(ret)

@api.route('/logout',methods=['GET'])
def logout():
    ret = {
        'id': '1',
        'name':'yxy',
        'password':'123'
    }
    return CommonResult.success(ret)


@api.route('/users',methods=['GET'])
def users():
    list = [
        {
            'id': '1',
            'name':'yxy1',
            'password':'123'
        },
        {
            'id': '2',
            'name':'yxy2',
            'password':'123'
        }
    ]
    ret = {
        'list': list,
        'total':len(list)
    }

    return CommonResult.success(ret)

@api.route('/check',methods=['GET'])
def check():
    ret = {
        'isValid': True
    }
    return CommonResult.success(ret)

@api.route('/wave',methods=['GET'])
def wave():
    wave = [[random.random()+c-0.5 for _ in range(150)] for c in range(18)]
    ret = {
        'wave': wave
    }
    return CommonResult.success(ret)

@api.route('/bcigo',methods=['GET'])
def bcigo():
    ret = {
    }
    return CommonResult.success(ret)

@api.route('/startPredict',methods=['GET'])
def startPredict():
    ret = {
    }
    return CommonResult.success(ret)

@api.route('/stopPredict',methods=['GET'])
def stopPredict():
    ret = {
        'subjectName': 'yxy'
    }
    return CommonResult.success(ret)

app.register_blueprint(api)
if __name__ == '__main__':
   app.run(debug=True,port=5005)