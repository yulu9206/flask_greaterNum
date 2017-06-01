from flask import Flask, render_template, session, request, redirect
import random  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
app.secret_key = 'ThisIsSecret'
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
def index():
  num = random.randrange(1, 100)
  session['num'] = num
  print session['num']       
  return render_template('index.html')# Return 'Hello World!' to the response.

@app.route('/guess', methods=['POST'])
def guess():
  guess = int(request.form['first'])
  if guess > session['num']:
	return render_template('index.html', result='Too High!')
  elif guess < session['num']:
	return render_template('index.html', result='Too Low!')
  else:
	return render_template('win.html', result=guess)

@app.route('/play_again')
def play_again():      
  return redirect('/')
app.run(debug=True)