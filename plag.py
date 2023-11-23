```
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
        logger.info("Received POST request for new plagiarism check")
        inputQuery = request.form['new_plagiarism_query']
        # Preprocess the input query
        # Perform the new plagiarism check
        # For demonstration, let's assume the new plagiarism score is a fixed value
        new_plagiarism_score = 75.00

        result = {
            "new_plagiarism_score": new_plagiarism_score
        }
        return jsonify(result)
    except Exception as e:
        logger.error("Exception caught: %s", str(e))
        return jsonify({"error": "An error occurred while processing your request."})

if __name__ == "__main__":
    logger.info("Starting web application")
    app.run()
```
    }
  ]
}
