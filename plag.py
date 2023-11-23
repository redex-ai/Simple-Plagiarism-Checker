import logging
from flask import Flask, request, render_template
import re
import math

app = Flask("__name__")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

q = ""

@app.route("/")
def loadPage():
    logger.info("Loading index.html")
    return render_template('index.html', query="")

@app.route("/", methods=['POST'])
def cosineSimilarity():
    try:
        logger.info("Received POST request")
        universalSetOfUniqueWords = []
        matchPercentage = 0

        ####################################################################################################

        inputQuery = request.form['query']
        lowercaseQuery = inputQuery.lower()

        queryWordList = re.sub("[^\w]", " ",lowercaseQuery).split()            #Replace punctuation by space and split
        # queryWordList = map(str, queryWordList)                    #This was causing divide by zero error

        for word in queryWordList:
            if word not in universalSetOfUniqueWords:
                universalSetOfUniqueWords.append(word)

        ####################################################################################################

        fd = open("database1.txt", "r")
        database1 = fd.read().lower()

        databaseWordList = re.sub("[^\w]", " ",database1).split()    #Replace punctuation by space and split
        # databaseWordList = map(str, databaseWordList)            #And this also leads to divide by zero error

        for word in databaseWordList:
            if word not in universalSetOfUniqueWords:
                universalSetOfUniqueWords.append(word)

        ####################################################################################################

        queryTF = []
        databaseTF = []

        for word in universalSetOfUniqueWords:
            queryTfCounter = 0
            databaseTfCounter = 0

            for word2 in queryWordList:
                if word == word2:
                    queryTfCounter += 1
            queryTF.append(queryTfCounter)

            for word2 in databaseWordList:
                if word == word2:
                    databaseTfCounter += 1
            databaseTF.append(databaseTfCounter)

        dotProduct = 0
        for i in range (len(queryTF)):
            dotProduct += queryTF[i]*databaseTF[i]

        queryVectorMagnitude = 0
        for i in range (len(queryTF)):
            queryVectorMagnitude += queryTF[i]**2
        queryVectorMagnitude = math.sqrt(queryVectorMagnitude)

        databaseVectorMagnitude = 0
        for i in range (len(databaseTF)):
            databaseVectorMagnitude += databaseTF[i]**2
        databaseVectorMagnitude = math.sqrt(databaseVectorMagnitude)

        matchPercentage = (float)(dotProduct / (queryVectorMagnitude * databaseVectorMagnitude))*100

        '''
        print queryWordList
        print
        print databaseWordList


        print queryTF
        print
        print databaseTF
        '''

        output = "Input query text matches %0.02f%% with database."%matchPercentage

        return render_template('index.html', query=inputQuery, output=output)
    except Exception as e:
        logger.error("Exception caught: %s", str(e))
        output = "Please Enter Valid Data"
        return render_template('index.html', query=inputQuery, output=output)

@app.route("/check_jaccard", methods=['POST'])
def jaccardSimilarity():
    try:
        logger.info("Received POST request for Jaccard similarity")
        inputQuery = request.form['jaccard_query']  # Change 'query' to 'jaccard_query'
        lowercaseQuery = inputQuery.lower()

        queryWordList = re.sub("[^\w]", " ", lowercaseQuery).split()  # Replace punctuation by space and split

        fd = open("database1.txt", "r")
        database1 = fd.read().lower()

        databaseWordList = re.sub("[^\w]", " ", database1).split()  # Replace punctuation by space and split

        querySet = set(queryWordList)
        databaseSet = set(databaseWordList)

        intersection = querySet.intersection(databaseSet)
        union = querySet.union(databaseSet)

        jaccardSimilarity = len(intersection) / len(union) * 100

        output = "Input query text has a Jaccard similarity of %0.02f%% with the database." % jaccardSimilarity

        return render_template('index.html', jaccard_query=inputQuery, jaccard_output=output)
    except Exception as e:
        logger.error("Exception caught: %s", str(e))
        output = "Please Enter Valid Data"
        return render_template('index.html', jaccard_query="", jaccard_output=output)


if __name__ == "__main__":
    logger.info("Starting web application")
    app.run()
