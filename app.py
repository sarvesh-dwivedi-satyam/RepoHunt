from flask import Flask, render_template, request
from services.github_api import search_repositories, search_issues

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    language = request.args.get('language', None)
    sort = request.args.get('sort', 'stars')
    
    repositories = []
    if query:
        repositories = search_repositories(query, language=language, sort=sort)
        
    return render_template('search.html', repositories=repositories, query=query)

@app.route('/issues')
def issues():
    query = request.args.get('q', 'python')
    language = request.args.get('language', None)
    
    issue_list = search_issues(query, language=language)
    return render_template('issues.html', issues=issue_list, query=query)

if __name__ == '__main__':
    app.run(debug=True)