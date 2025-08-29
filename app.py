import os
from flask import Flask, send_from_directory, abort

app = Flask(__name__)

@app.route("/download/<filename>")
def download(filename):
    music_dir = os.path.join(app.root_path, "static/musicas")
    file_path = os.path.join(music_dir, filename)
    if not os.path.isfile(file_path):
        abort(404)
    return send_from_directory(music_dir, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)