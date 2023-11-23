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
    # ... (existing cosineSimilarity code) ...

@app.route("/check_jaccard", methods=['POST'])
def jaccardSimilarity():
    # ... (existing jaccardSimilarity code) ...

@app.route('/new_plagiarism_check', methods=['POST'])
def newPlagiarismCheck():
    try:
        logger.info("Received POST request for new plagiarism checking technique")
        # Implement the new plagiarism checking logic here
        # For example, let's assume it's a simple word count comparison
        inputQuery = request.form['new_plagiarism_query']
        databaseText = open("database1.txt", "r").read().lower()

        # Count words in the input query and database text
        inputQueryWordCount = len(re.findall(r"\w+", inputQuery))
        databaseWordCount = len(re.findall(r"\w+", databaseText))

        # Calculate the plagiarism score (this is just a placeholder for the actual algorithm)
        plagiarismScore = min(inputQueryWordCount, databaseWordCount) / max(inputQueryWordCount, databaseWordCount) * 100

        output = {
            'plagiarism_score': plagiarismScore
        }
        return jsonify(output)
    except Exception as e:
        logger.error("Exception caught: %s", str(e))
        return jsonify({'error': 'An error occurred during the plagiarism check'}), 500

if __name__ == "__main__":
    logger.info("Starting web application")
    app.run()
