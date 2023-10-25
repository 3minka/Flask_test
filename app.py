from flask import Flask

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

if __name__ == "__main__":
    app.run()