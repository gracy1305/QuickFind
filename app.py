from flask import Flask, render_template, request
from scraper import get_search_results
 
 # Flask app setup
app = Flask(__name__)
 
 # Google API credentials
API_KEY = "your-API-KEY"
CSE_ID = "your-CSE-ID"
 
@app.route('/')
def home():
     return render_template('index.html', home_page=True)
 
@app.route('/search')
def search():
     query = request.args.get('query', '')
     category = request.args.get('category', 'web')
     start = int(request.args.get('start', 1))
 
     results, next_start, previous_start = get_search_results(query, category, start, API_KEY, CSE_ID)
 
     return render_template(
         'search_results.html',
         query=query,
         results=results,
         next_start=next_start,
         previous_start=previous_start,
         category=category
     )
 
if __name__ == '__main__':
     app.run(debug=True)