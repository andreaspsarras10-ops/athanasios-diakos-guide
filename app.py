import os
from flask import Flask, render_template

app = Flask(__name__)

# Αυτή η λειτουργία σκανάρει αυτόματα τον φάκελο static για αρχεία εικόνων και βίντεο
def get_static_files():
    static_dir = os.path.join(app.root_path, 'static')
    if not os.path.exists(static_dir):
        return [], []
    
    all_files = os.listdir(static_dir)
    
    # Φιλτράρισμα εικόνων (περιλαμβάνει και HEIC από iPhone)
    img_ext = ('.jpg', '.jpeg', '.png', '.webp', '.jfif', '.heic', '.JPG', '.JPEG', '.PNG', '.HEIC')
    images = [f for f in all_files if f.endswith(img_ext)]
    
    # Φιλτράρισμα βίντεο (περιλαμβάνει και MOV από iPhone)
    vid_ext = ('.mp4', '.mov', '.avi', '.MP4', '.MOV')
    videos = [f for f in all_files if f.endswith(vid_ext)]
    
    return images, videos

@app.route("/")
def home():
    images, videos = get_static_files()
    return render_template("index.html", images=images, videos=videos)

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/reasonstovisit")
def reasonstovisit():
    return render_template("reasonstovisit.html")

if __name__ == "__main__":
    app.run(debug=True)
