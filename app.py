from flask import Flask, request, send_file
from google.cloud import storage
import os

app = Flask(__name__)

# Read bucket name from environment variable
BUCKET = os.environ.get("BUCKET")

if not BUCKET:
    raise ValueError("BUCKET environment variable is not set")

client = storage.Client()
bucket = client.bucket(BUCKET)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]

        if not file:
            return "No file uploaded", 400

        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)

        return "Uploaded successfully!"

    return """
    <h2>Upload file</h2>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit">
    </form>
    """

@app.route("/download/<filename>")
def download(filename):
    blob = bucket.blob(filename)
    blob.download_to_filename(filename)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

