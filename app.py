from flask import Flask
from flask import jsonify, request ## api 만들기 위한 라이브러리 


app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<h1>hello, world!</h1>"

@app.route("/<username>") # get 데이터, url 데이터로 
def hello_user(username):
    return f"<h1> hello, {username}! </h1>"


@app.route("/feed/<int:feed_id>") # get 데이터, url 데이터로 
def show_feed(feed_id):
    return f"<h1> FeedID: {feed_id} </h1>"


############################################### api db 만들기 수업 10/26
# CRUD : CREAT(POST), READ(GET), UPDATA(UPDATAE), DELETE(DEL)
# GET : 데이터를 요청할 때,
# POST : CREATE, 데이터 생성할 때,
@app.route("/api/v1/feeds", methods=['GET']) # 요청을 줘 api 입니다.

def get_all_feeds():  # 전체 데이터를 주자

    # DB에서 불러주는 것으로 
    data = {
        'status' : 'success',
        'feed' : {
            "feed1" : "data",
            "feed2" : "data"
        }
    }
    return jsonify(data)

# JSON -> 프로토콜, 컴퓨터와 컴퓨터간의 상호작용을 위해 만들어짐. 
# 핸드폰 -> 조명 껐다 켰다 할 수 있는 거의 소통 방식 

## POST
@app.route('api/v1/feeds', method=['POST'])
def create_feed():
    # request : 유저가 보낸 데이터
    subject = request.form['subject']
    content = request.form['content']

    return jsonify({"result" : "success"})
###############################################

if __name__ == "__main__":
    app.run()

#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