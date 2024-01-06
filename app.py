from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from src.data_summarization import predict_summary  # You need to implement this function

app = Flask(__name__)

# Set the path where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allow only specific file extensions
ALLOWED_EXTENSIONS = {'pdf', 'jpg','png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = f"{app.config['UPLOAD_FOLDER']}/{filename}"
        file.save(filepath)

        # Call your predict_summary function here
        summary,text = predict_summary(filepath)

        return render_template('index.html', summary=summary, text = text)

    return render_template('index.html', error='Invalid file format')

if __name__ == '__main__':
    app.run(debug=True)


