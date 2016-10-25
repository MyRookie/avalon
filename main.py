from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def login():
    print "uid"
    return render_template('main.html')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == "__main__":
    app.run()
