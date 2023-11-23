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

@app.route('/new_plagiarism_check', methods=['POST'])
def newPlagiarismCheck():
    try:
        logger.info("Received POST request for new plagiarism checking technique")
        # Implement the new plagiarism checking logic here
        # For example, let's assume it's a simple word count comparison
        inputQuery = request.form['new_plagiarism_query']
        databaseText = open("database1.txt", "r").read().lower()

        # Tokenize the input and the database text
        inputTokens = set(re.sub("[^\w]", " ", inputQuery.lower()).split())
        databaseTokens = set(re.sub("[^\w]", " ", databaseText).split())

        # Calculate the new plagiarism score (example logic)
        commonWords = inputTokens.intersection(databaseTokens)
        totalWords = inputTokens.union(databaseTokens)
        plagiarismScore = len(commonWords) / len(totalWords) * 100

        # Return the result as JSON
        result = {
            'plagiarism_score': plagiarismScore
        }
        return jsonify(result)
    except Exception as e:
        logger.error("Exception caught: %s", str(e))
        return jsonify({'error': 'An error occurred during the plagiarism check.'}), 500

if __name__ == "__main__":
    logger.info("Starting web application")
    app.run()
