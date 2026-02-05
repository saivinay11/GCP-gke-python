from flask import Flask, request
from google.cloud import storage
import os

app = Flask(__name__)

# Read bucket name from environment variable
BUCKET = os.environ.get("BUCKET")

# Safety check (helps debugging)
if not BUCKET:
    raise ValueError("BUCKET environment variable not set")

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=

