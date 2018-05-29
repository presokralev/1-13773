from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
    <head>
        <title>Modern Pentathlon</title>
        <style>
            body {
                font-family: Helvetica, Arial, sans-serif;
                font-variant: small-caps;
            }
            #name{
                text-align:center;
            }
            .list {
                list-style-type: none;
                
                background-color:powder-blue;
                text-align:center;
            }
            .list li a{
                display: inline-block;
                background-color: #2288ff;
                color: white;
                padding: 20px 30px;
                min-width: 100px;
               
                list-style-type:none;
                float:left;
                margin:20px;
            } 
        </style>
    </head>
    <body>
        <h2 id="name">Модерен петобой!</h2>
        <ul class="list">
                    <li><a href="http://127.0.0.1:5000/swimming">ПЛУВАНЕ</a></li>
                    <li><a href="http://127.0.0.1:5000/running">БЯГАНЕ</a></li>
                    <li><a href="http://127.0.0.1:5000/fencing">ФЕХТОВКА</a></li>
                    <li><a href="http://127.0.0.1:5000/shooting">СТРЕЛБА</a></li>
                    <li><a href="http://127.0.0.1:5000/horseriding">КОННА ЕЗДА</a></li>
                    <li><a href="http://127.0.0.1:5000/contacts">КОНТАКТИ</a></li>
        </ul>
           
        
       
    </body>
    </html>
    """


@app.route("/swimming")
def swimming():
    return"""
    
    """

@app.route("/running")
def running():
    return """

    """


@app.route("/fencing")
def fencing():
    return """

    """


@app.route("/shooting")
def shooting():
    return """

    """


@app.route("/horseriding")
def horseriding():
    return """

    """

@app.route("/contacts")
def contacts():
    return """

    """
if __name__ == "__main__":
    app.run()
