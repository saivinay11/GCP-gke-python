from flask import Flask, request, send_file
from google.cloud import storage
import os

app = Flask(__name__)
BUCKET = os.environ["BUCKET_NAME"]

client = storage.Client()
bucket = client.bucket(BUCKET)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        blob = bucket.blob(f.filename)
        blob.upload_from_file(f)
        return "Uploaded successfully!"

    return '''
    <h2>Upload file</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit">
    </form>
    '''

@app.route("/download/<name>")
def download(name):
    blob = bucket.blob(name)
    blob.download_to_filename(name)
    return send_file(name)

app.run(host="0.0.0.0", port=80)
