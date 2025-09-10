from flask import Flask, request, render_template
from detect import detect   # renamed from main_ds_test.py → detect.py

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("Login/index.html")

@app.route("/login")
def Login():
    return render_template("Login/index.html")

@app.route('/home_page', methods=["GET", "POST"])
def Home():
    return render_template("Home/home.html")

@app.route('/about')
def about():
    return render_template("About/about.html")

@app.route('/upload_image')
def upload_image():
    return render_template("Upload_Image/upload_image.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    img = request.files['in_img']
    i_path = "static/uploaded_files/image.jpg"
    img.save(i_path)

    msg, cyst_count = detect(i_path)   # new detect function returns image + cyst count
    if msg.startswith("ERROR:"):
        return f"<h1>{msg}</h1>"
    else:
        return render_template("Result/result.html", image_path=msg, content=cyst_count)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
