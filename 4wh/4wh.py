import json
from random import randint
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/member')
def member():
    with open('templates/members.json', 'r', encoding='utf') as f:
        data = json.loads(f.read())
        data = data['members'][randint(0, 5)]
    return render_template('member.html', data=data)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')