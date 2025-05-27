from flask import Flask, render_template, abort
import os

app = Flask(__name__)
POSTS_DIR = 'posts'

@app.route("/")
def index():
    # posts フォルダ内のファイル名（日付）一覧を取得
    posts = sorted(os.listdir(POSTS_DIR), reverse=True)
    return render_template("index.html", posts=posts)

@app.route("/posts/<post_id>")
def post(post_id):
    path = os.path.join(POSTS_DIR, post_id + ".md")
    if not os.path.exists(path):
        abort(404)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return render_template("post.html", post_id=post_id, content=content)
if __name__ == '__main__':
    app.run(debug=True)
