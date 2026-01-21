from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h1>Hello, world!</h1>"

@app.route('/users/<string:username>')
def show_user_profile(username: str) -> str:
    return f'Profilo di {username}'

@app.route('/posts/<int:post_id>')
def show_post(post_id: int) -> str:
    return f'Post {post_id}'

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='John Doe'))
    print(url_for('show_post', post_id=42))