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
    
    Got it! Here's an extended sample text to thoroughly test your predictive text AI:

---

### **The Evolution of Artificial Intelligence: From Theory to Reality**

Artificial Intelligence (AI) has rapidly evolved from a theoretical concept into a transformative force that drives global innovation. The journey of AI began in the 1950s, when pioneers like Alan Turing and John McCarthy laid the foundation for intelligent machines. Over the decades, AI has progressed from symbolic reasoning models to modern deep learning architectures, revolutionizing fields such as healthcare, finance, and autonomous systems.

AI’s ability to process vast amounts of data has enabled breakthroughs in predictive analytics, automation, and cognitive computing. Machine learning models, particularly neural networks, have empowered systems to recognize patterns, optimize workflows, and anticipate future trends. Natural Language Processing (NLP) has played a crucial role in AI's development, allowing machines to understand and generate human language with remarkable accuracy.

One of the most significant milestones in AI is **predictive text technology**, which has improved human-computer interaction. Predictive text models analyze previous user input, identify contextual patterns, and suggest appropriate words or phrases. This has significantly enhanced productivity by reducing typing time and improving communication efficiency. AI-powered predictive text is now widely used in messaging apps, search engines, and assistive technologies, making everyday digital interactions more seamless.

### **Key Advancements in AI: The Role of Deep Learning and Neural Networks**

The advent of **deep learning** has marked a paradigm shift in AI research and applications. Deep learning models, inspired by the structure of the human brain, consist of multiple layers of artificial neurons that process and analyze data hierarchically. Convolutional Neural Networks (CNNs) have enabled remarkable improvements in **computer vision**, allowing machines to recognize objects, detect anomalies, and even generate high-quality images.

Similarly, **transformer-based models** such as GPT (Generative Pre-trained Transformer) and BERT (Bidirectional Encoder Representations from Transformers) have revolutionized **natural language understanding**. These models leverage massive datasets and complex architectures to generate coherent text, translate languages, and answer questions with human-like fluency. AI-driven chatbots and virtual assistants have become essential tools for customer service, healthcare diagnostics, and knowledge retrieval.

### **Challenges and Ethical Considerations in AI Deployment**

Despite its rapid progress, AI development presents several ethical challenges. Issues related to **bias in machine learning models**, **data privacy**, and **AI-generated misinformation** require careful regulation. AI systems often reflect biases present in training data, leading to unintended discriminatory outcomes. Ensuring fair and transparent AI applications remains a priority for researchers and policymakers.

Data privacy is another pressing concern. AI models rely on extensive datasets for training, raising questions about the security and ethical use of personal information. Organizations must implement robust encryption and privacy-preserving techniques to protect user data while maintaining AI’s effectiveness.

The rise of AI-generated misinformation highlights the importance of **content moderation** and **fact-checking mechanisms**. As AI systems become more advanced, distinguishing between human-written and AI-generated content poses a growing challenge. Responsible AI development must incorporate safeguards against the spread of false information.

### **The Future of AI: Collaboration Between Humans and Machines**

AI's trajectory suggests that it will continue to shape industries and redefine how humans interact with technology. Instead of replacing human intelligence, AI serves as an augmentation tool, empowering individuals to solve complex problems, automate routine tasks, and enhance decision-making.

Emerging AI applications include **AI-powered creativity**, where machines compose music, generate artwork, and write poetry. AI-driven simulations enable realistic training environments for professionals in medicine, engineering, and cybersecurity. Autonomous systems, such as **self-driving cars**, exemplify AI’s potential to reshape transportation while minimizing human intervention.

In the coming decades, human-AI collaboration will be fundamental to unlocking AI’s full potential. Ethical frameworks, interdisciplinary research, and responsible deployment will ensure AI remains beneficial to society. AI-powered predictive text systems, like the one you’re developing, exemplify how technology enhances efficiency while keeping communication natural and intuitive.

---

This extended text covers diverse sentence structures, technical terms, real-world applications, and ethical considerations—perfect for testing your predictive text AI! 🚀 Let me know if you need further refinements or specific types of sample data.
"""
    
    predictor = SimpleNextWordPredictor()
    predictor.train(sample_text)
    predictor.interactive_prediction()

if __name__ == "__main__":
    main()