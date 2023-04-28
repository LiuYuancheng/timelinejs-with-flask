
from flask import Flask
from flask import render_template
from flask import g
from flask import Response
from flask import request
from flask import redirect
from flask import url_for, send_from_directory

app = Flask(__name__)

@app.route("/")
def render_timeline():
    eventJson = {
        "title": {
                "text": {
                    "headline": "Example timeline",
                    "text":     "Events 123 in the 7th century \
                        from https://en.wikipedia.org/wiki/Timeline_of_the_Middle_Ages"
                }
        },
        "events": [
            {
                "start_date": {
                    "year":			"2015",
                    "month":		"01"
                },
                "media": {
                    "url": "static/img/stick-man.png"
                },
                "text": {
                    "headline": "Example with own image",
                    "text": "Long conflict leaves both empires exhausted and unable to cope with the newly united Arab armies under Islam in the 630s"
                }
            },
            {
                "start_date": {
                    "year":			"2015",
                    "month":		"02"
                },
                "end_date": {
                    "year":			"2015",
                    "month":		"03"
                },
                "media": {
                    "url": "https://en.wikipedia.org/wiki/Grand_Canal_(China)"
                },
                "background": {
                    "opacity":"50",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Sui_Wendi_Tang.jpg"
                },
                "text": {
                    "headline": "Grand Canal in China is fully completed",
                    "text": "Its main role throughout its history was the transport of grain to the capital."
                }
            }
    
        ]
    }
    return render_template('index_v1.html', posts=eventJson)

if __name__ == "__main__":	
	app.run(port = 5000, host = '0.0.0.0', use_reloader=True, threaded=True, debug=True)