import logging
from flask import Flask, request, render_template, jsonify
import re
import math

app = Flask("__name__")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

q = ""

@app.route("/")
def loadPage():
    logger.info("Loading index.html")
    return render_template('index.html', query="")

@app.route("/", methods=['POST'])
def cosineSimilarity():
    # ... (existing cosineSimilarity code remains unchanged) ...

@app.route("/check_jaccard", methods=['POST'])
def jaccardSimilarity():
    # ... (existing jaccardSimilarity code remains unchanged) ...

@app.route("/new_plagiarism_check", methods=['POST'])
def newPlagiarismCheck():
    try:
        logger.info("Received POST request for new plagiarism checking technique")
        # Implement the new plagiarism checking logic here
        # For example, let's assume it's a simple word count comparison
        inputQuery = request.form['new_plagiarism_query']
        lowercaseQuery = inputQuery.lower()

        queryWordList = re.sub("[^\w]", " ", lowercaseQuery).split()

        fd = open("database1.txt", "r")
        database1 = fd.read().lower()

        databaseWordList = re.sub("[^\w]", " ", database1).split()

        # Calculate the new plagiarism score (this is just a placeholder example)
        plagiarismScore = float(len(set(queryWordList) & set(databaseWordList))) / len(set(queryWordList) | set(databaseWordList)) * 100

        output = {
            'new_plagiarism_query': inputQuery,
            'new_plagiarism_score': plagiarismScore
        }

        return jsonify(output)
    except Exception as e:
        logger.error("Exception caught: %s", str(e))
        return jsonify({'error': 'An error occurred during the new plagiarism check.'})

if __name__ == "__main__":
    logger.info("Starting web application")
    app.run()
