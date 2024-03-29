from flask import Flask, request, render_template
from threading import Thread
import os

app = Flask('')

def append_new_title(new_title):
    with open("movies_titles.txt", "a") as file:
        if file.tell() != 0:
            file.write("\n")
        file.write(new_title.lower())

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/add_movie', methods=['POST'])
def add_movie():
    new_movie_title = request.form.get('text_box')
    if new_movie_title:
        append_new_title(new_movie_title)
        return "Movie added successfully!"
    else:
        return "Missing movie title!", 400

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

if __name__ == "__main__":
    keep_alive()