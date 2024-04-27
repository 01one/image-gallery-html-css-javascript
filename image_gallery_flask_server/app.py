from flask import Flask, render_template
import glob
import os

app = Flask(__name__)

@app.route('/')
def image_gallery():
    image_folder = "static/images/"
    file_paths = glob.glob(os.path.join(image_folder, '*.jpg'))
    file_names = [os.path.basename(file_path) for file_path in file_paths]
    return render_template('image-gallery.html', file_names=file_names)

if __name__ == '__main__':
    app.run(debug=True)
