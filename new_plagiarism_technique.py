```
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def preprocess_text(text):
    """Preprocess the input text by converting to lowercase and removing punctuation."""
    try:
        text = text.lower()
        text = re.sub(r'[^\
\w\s]', '', text)
        return text.split()
    except Exception as e:
        logger.error('Error during text preprocessing: %s', e)
        raise


def calculate_plagiarism_score(text1, text2):
    """Calculate the plagiarism score between two pieces of text."""
    try:
        # Preprocess the texts
        words1 = preprocess_text(text1)
        words2 = preprocess_text(text2)

        # Calculate the plagiarism score
        common_words = set(words1).intersection(set(words2))
        total_words = set(words1).union(set(words2))
        score = len(common_words) / len(total_words) * 100

        logger.info('Plagiarism score calculated: %f', score)
        return score
    except Exception as e:
        logger.error('Error calculating plagiarism score: %s', e)
        raise

```