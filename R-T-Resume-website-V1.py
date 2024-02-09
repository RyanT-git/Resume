from flask import *
app = Flask(__name__)

myInfo = """
<!DOCTYPE html>
<html>
<body>
<h1>About Me</h1>
<h2> [info] </h2>
</body>
</html>
"""


@app.route('/')
def you_found_me():
   return render_template('resume.html')
   
@app.route('/about')
def upload():
	return myInfo

if __name__ == '__main__':
   app.run('0.0.0.0', port = 4242, debug = True)

