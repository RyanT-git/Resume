from flask import *
app = Flask(__name__)

@app.route('/')
def you_found_me():
   return render_template('resume.html')

@app.route('/codepath')
def pdf_viewer():
	return redirect("./static/Course Overview - CYB102 _ Intermediate Cybersecurity _ CodePath Courses.pdf")

if __name__ == '__main__':
   app.run('0.0.0.0', port = 4242, debug = True)

