from flask import Flask, render_template, request, escape
from vsearch import search4letters
app = Flask(__name__)

def log_request(req: 'flask_requst', res: str) -> None:
		with open('vsearch.log', 'a') as logfile:
			print(req.form, req.remote_addr, req.user_agent, res, file=logfile, sep='|')


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
def view_the_log() -> 'html':
	list_log = []
	with open('vsearch.log') as logfile:
		for line in logfile:
			list_log.append([])
			for item in line.split('|'):
				list_log[-1].append(escape(item))
	titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
	return render_template('viewlog.html',
							the_titla='View Log',
							the_row_titles=titles,
							the_data=list_log,)

if __name__ == '__main__':
        app.run(debug=True)

