import random
from collections import defaultdict

class SimpleNextWordPredictor:
    def __init__(self):
        self.word_frequencies = defaultdict(lambda: defaultdict(int))
        self.total_words = defaultdict(int)
    
    def train(self, text):
        # Preprocess the text
        words = text.lower().split()
        
        # Build a model of word frequencies
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.word_frequencies[current_word][next_word] += 1
            self.total_words[current_word] += 1
    
    def predict_next_word(self, current_word, num_predictions=3):
        current_word = current_word.lower()
        
        # If we've never seen this word before
        if current_word not in self.word_frequencies:
            return ["[unknown]"]
        
        # Get frequencies of all words that followed the current word
        next_word_counts = self.word_frequencies[current_word]
        total = self.total_words[current_word]
        
        # Calculate probabilities and sort by most likely
        predictions = [(next_word, count / total) 
                        for next_word, count in next_word_counts.items()]
        predictions.sort(key=lambda x: x[1], reverse=True)
        
        # Return the top predictions
        return [word for word, prob in predictions[:num_predictions]]
    
    def interactive_prediction(self):
        print("Enter a word and I'll predict what comes next!")
        print("Type 'quit' to exit.")
        
        while True:
            user_input = input("> ")
            if user_input.lower() == 'quit':
                break
                
            predictions = self.predict_next_word(user_input)
            print(f"After '{user_input}', I predict: {', '.join(predictions)}")


# Example usage
def main():
    # Sample training text
    sample_text = """
    Python is a programming language that lets you work quickly
    and integrate systems more effectively. Python is powerful and
    fast. Python runs on Windows, Linux, Mac OS and many other platforms.
    """
    predictor = SimpleNextWordPredictor()
    predictor.train(sample_text)
    predictor.interactive_prediction()
def main():
    # Much larger sample text
    sample_text = """
    The sun was setting behind the mountains, casting long shadows across the valley. The air was cool and crisp, filled with the scent of pine trees. I walked along the winding path, enjoying the peace and quiet. My friend was waiting for me at the cabin, probably wondering what was taking me so long.

    Artificial intelligence has revolutionized many industries in recent years. Machine learning algorithms can analyze vast amounts of data to identify patterns and make predictions. Deep learning systems have achieved remarkable results in image recognition, natural language processing, and game playing. The field of AI continues to evolve rapidly, with new breakthroughs announced almost daily.

    My favorite books include science fiction novels, mystery thrillers, and historical biographies. I love reading about distant worlds, complex characters, and dramatic plot twists. My collection has grown over the years, filling several bookshelves in my home. My sister often borrows books from me, while my brother prefers audiobooks during his daily commute.

    Python is a versatile programming language that can be used for web development, data analysis, artificial intelligence, and scientific computing. Many beginners start with Python because of its readable syntax and extensive libraries. Python runs on Windows, Linux, Mac OS, and many other platforms. My colleagues often use Python for their daily tasks.

    The recipe calls for flour, sugar, eggs, and butter. Mix the dry ingredients first, then add the wet ingredients gradually. Bake at 350 degrees for 25 minutes or until golden brown. My grandmother taught me this recipe when I was just a child. My family requests these cookies for every holiday gathering.

    I need to buy milk, bread, eggs, and vegetables from the grocery store. My shopping list also includes pasta, sauce, and cheese for dinner tomorrow night. My budget for groceries this week is rather tight, so I'll need to watch for sales and discounts.
    """
    
    predictor = SimpleNextWordPredictor()
    predictor.train(sample_text)
    predictor.interactive_prediction()

if __name__ == "__main__":
    main()
