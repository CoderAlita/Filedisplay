from flask import Flask

app= Flask(__name__)

@app.route("/display")
def file_diaplay():

    return "<p>file received </p>"

if __name__ == '__main__' :
    
    app.run(debug = True)