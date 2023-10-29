from flask import Flask, render_template, request, jsonify
from pytube import YouTube
from pydub import AudioSegment

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play_audio", methods=["POST"])
def play_audio():
    video_link = request.form["videoLink"]
    try:
        yt = YouTube(video_link)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_url = audio_stream.url

        return jsonify({"success": True, "audioURL": audio_url})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
