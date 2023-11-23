import logging
from flask import Flask, request, render_template
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
    # Existing cosine similarity code...

@app.route("/check_jaccard", methods=['POST'])
def jaccardSimilarity():
    # Existing Jaccard similarity code...

@app.route("/new_plagiarism_check", methods=['POST'])
def newPlagiarismCheck():
    try:
        logger.info("Received POST request for new plagiarism checking technique")
        # Implement the new plagiarism checking algorithm here
        # ...

        # Example output (replace with actual output from the new algorithm)
        output = "New plagiarism check result: 75% match"

        return render_template('index.html', new_plagiarism_check_output=output)
    except Exception as e:
        logger.error("Exception caught in new plagiarism check: %s", str(e))
        output = "An error occurred during the new plagiarism check"
        return render_template('index.html', new_plagiarism_check_output=output)

if __name__ == "__main__":
    logger.info("Starting web application")
    app.run()
