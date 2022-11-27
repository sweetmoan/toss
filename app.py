from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get():
    if request.method == "POST":
        url = request.form['yt-url']
        yt = YouTube(url)
        st = yt.streams.get_highest_resolution()
        st.download()
        return render_template("index.html", title=yt.title, url=yt.title, thumbail_url=yt.thumbnail_url)

@app.route('/download/<url>', methods=['POST'])
def download(url):
    if request.method == "POST":
        return send_file(url+".mp4", as_attachment=True)



if __name__=="__main__":
    app.run(debug=True,port='80')
