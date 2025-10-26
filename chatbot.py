#!/usr/bin/env python3
"""
A simple chatbot application with pattern matching and conversation logic.
"""

import re
import random
from datetime import datetime


class SimpleChatbot:
    """A basic chatbot that responds to user inputs using pattern matching."""
    
    def __init__(self):
        self.name = "ChatBot"
        self.patterns = {
            r'\b(hi|hello|hey)\b': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!"
            ],
            r'\b(how are you|how\'s it going)\b': [
                "I'm doing great, thank you for asking!",
                "I'm functioning perfectly! How about you?",
                "I'm here and ready to chat!"
            ],
            r'\b(what is your name|who are you)\b': [
                f"I'm {self.name}, your friendly chatbot!",
                f"My name is {self.name}. Nice to meet you!",
                f"I go by {self.name}. How can I assist you?"
            ],
            r'\b(what time|time is it)\b': [
                f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                f"It's {datetime.now().strftime('%I:%M %p')} right now"
            ],
            r'\b(help|what can you do)\b': [
                "I can chat with you! Try asking me about the time, how I'm doing, or just say hello!",
                "I'm here to have a conversation. Ask me questions or just chat!",
                "I can respond to greetings, tell you the time, and have basic conversations!"
            ],
            r'\b(bye|goodbye|see you)\b': [
                "Goodbye! Have a great day!",
                "See you later! It was nice chatting with you!",
                "Bye! Come back anytime!"
            ],
            r'\b(thank you|thanks)\b': [
                "You're welcome!",
                "Happy to help!",
                "Anytime!"
            ],
        }
        
        self.default_responses = [
            "I'm not sure I understand. Can you rephrase that?",
            "Interesting! Tell me more.",
            "I see. What else would you like to know?",
            "That's a good question! I'm still learning.",
            "Hmm, I'm not quite sure about that. Try asking something else!"
        ]
    
    def get_response(self, user_input):
        """Get a response based on user input using pattern matching."""
        user_input_lower = user_input.lower()
        
        # Check each pattern
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input_lower, re.IGNORECASE):
                return random.choice(responses)
        
        # Default response if no pattern matches
        return random.choice(self.default_responses)
    
    def chat(self):
        """Start an interactive chat session."""
        print(f"\n{self.name}: Hello! I'm {self.name}. Type 'quit' or 'exit' to end our conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit']:
                    print(f"\n{self.name}: Goodbye! Thanks for chatting with me!\n")
                    break
                
                response = self.get_response(user_input)
                print(f"{self.name}: {response}\n")
                
            except (KeyboardInterrupt, EOFError):
                print(f"\n\n{self.name}: Goodbye! Thanks for chatting with me!\n")
                break


def main():
    """Main function to run the chatbot."""
    chatbot = SimpleChatbot()
    chatbot.chat()


if __name__ == "__main__":
    main()
