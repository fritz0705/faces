# coding: utf-8

import bottle
import pymongo
import jinja2

static_file = bottle.static_file

app = bottle.Bottle()
db = None
env = jinja2.Environment(loader=jinja2.FileSystemLoader("views/"))

def view(name, **kwargs):
	return env.get_template(name + '.html').render(**kwargs)

@app.route("/")
def show_all():
	faces = db.faces.find()
	return view("index", faces=faces)

@app.route("/<face:int>")
def show_face(face):
	face = db.faces.find_one({"number": face})
	return view("face", face=face)

@app.route("/<face:int>/full")
def show_full_face(face):
	return static_file("{0}.jpg".format(face), root='faces/', mimetype="image/jpeg")

@app.route("/<face:int>/thumb")
def show_thumb_face(face):
	return static_file("{0}.jpg".format(face), root='thumbs/', mimetype="image/jpeg")

@app.route("/static/<path:path>")
def static(path):
	return static_file(path, root='static/')

