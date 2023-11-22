```
import logging
from flask import Flask, request, render_template
import re
import math

app = Flask("__name__")

# Initialize logging with the desired format and level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

q = ""

@app.route("/")
def loadPage():
    logger.info("Loading index.html")
    return render_template('index.html', query="")

@app.route("/", methods=['POST'])
def cosineSimilarity():
    try:
        logger.info("Received POST request for cosine similarity")
        universalSetOfUniqueWords = []
        matchPercentage = 0

        # Rest of the code remains unchanged...

if __name__ == "__main__":
    logger.info("Starting web application")
    app.run()
```