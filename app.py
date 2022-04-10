from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

from pymongo import MongoClient

import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.kxazb.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

import hashlib
hashing = hashlib.sha256()


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route("/users_signup", methods=["POST"])
def users():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']

    doc = {
        'id': id_receive,
        'pw': pw_receive,
        'name': name_receive,
        'email': email_receive,
    }

    db.users.insert_one(doc)

    return jsonify({'msg':'회원 가입 완료!'})




@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies':movie_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)