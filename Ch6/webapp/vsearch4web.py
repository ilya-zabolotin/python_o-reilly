from flask import Flask, render_template, request, escape
from vsearch import search4letters
app = Flask(__name__)

def log_request(req: 'flask_requst', res: str) -> None:
        with open('vsearch.log', 'a') as logfile:
                print(req, res, file=logfile)
                

@app.route('/search4', methods=['POST'])
def do_search () -> 'html':
        phrase = request.form['phrase']
        letters = request.form['letters']
        title = 'Here are your resuts: '
        results = str(search4letters(phrase, letters))
        log_request(request, results)
        return render_template('results.html',
                               the_title=title,
                               the_phrase=phrase,
                               the_letters=letters,
                               the_results=results,)

@app.route('/')
@app.route('/entry')
def enrty_page() -> 'html':
        return render_template('entry.html', the_title='Welcome to search4vowels on the web!')
		
		
@app.route('/viewlog')
def view_the_log() -> str:
	with open('vsearch.log') as logfile:
		contents = logfile.read()
	return escape(contents)




if __name__ == '__main__':
        app.run(debug=True)

