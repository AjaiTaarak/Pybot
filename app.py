from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


app = Flask(__name__)
app = Flask(static_folder='D:/College/PSGCAS/flask-chatterbot-master/static',import_name='static')
english_bot = ChatBot("Buddy", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
 # trainer.train("chatterbot.corpus.english.greetings")
 # trainer.train("chatterbot.corpus.english.conversations")



trainer = ListTrainer(english_bot)
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")
trainer.train([
'Hi',
'Hello',
'What is Python?',
'Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.',
'Uses of python',
'web development (server-side),software development,mathematics,system scripting.',
'What is List',
'A list is a collection which is ordered and changeable. In Python lists are written with square brackets.',
'List',
'A list is a collection which is ordered and changeable. In Python lists are written with square brackets.',
'Tuple',
'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.',
'What is Tuple',
'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.',
'What is the difference between list and tuples?',
'Lists are mutable i.e they can be edited. Tuples are immutable (tuples are lists which can’t be edited).',
'What are the key features of Python?',
'Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.',
'What type of language is python? Programming or scripting',
'Python is capable of scripting, but in general sense, it is considered as a general-purpose programming language.',
'How is Python an interpreted language',
'An interpreted language is any programming language which is not in machine level code before runtime. Therefore, Python is an interpreted language.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])


@app.route("/")
def home():
    return render_template("index1.html")

@app.route('/index.html/')
def about():
    return render_template('index.html')

@app.route('/index2.html/')
def about2():
    return render_template('index2.html')

@app.route('/index3.html/')
def about3():
    return render_template('index3.html')

@app.route('/contact.html/')
def about4():
    return render_template('contact.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()



