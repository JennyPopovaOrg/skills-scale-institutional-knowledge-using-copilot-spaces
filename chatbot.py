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
        # Pre-compile regex patterns for better performance
        self.patterns = [
            (re.compile(r'\b(hi|hello|hey)\b', re.IGNORECASE), [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!"
            ]),
            (re.compile(r'\b(how are you|how\'s it going)\b', re.IGNORECASE), [
                "I'm doing great, thank you for asking!",
                "I'm functioning perfectly! How about you?",
                "I'm here and ready to chat!"
            ]),
            (re.compile(r'\b(what is your name|who are you)\b', re.IGNORECASE), [
                f"I'm {self.name}, your friendly chatbot!",
                f"My name is {self.name}. Nice to meet you!",
                f"I go by {self.name}. How can I assist you?"
            ]),
            (re.compile(r'\b(what time|time is it)\b', re.IGNORECASE), 'time'),
            (re.compile(r'\b(help|what can you do)\b', re.IGNORECASE), [
                "I can chat with you! Try asking me about the time, how I'm doing, or just say hello!",
                "I'm here to have a conversation. Ask me questions or just chat!",
                "I can respond to greetings, tell you the time, and have basic conversations!"
            ]),
            (re.compile(r'\b(bye|goodbye|see you)\b', re.IGNORECASE), [
                "Goodbye! Have a great day!",
                "See you later! It was nice chatting with you!",
                "Bye! Come back anytime!"
            ]),
            (re.compile(r'\b(thank you|thanks)\b', re.IGNORECASE), [
                "You're welcome!",
                "Happy to help!",
                "Anytime!"
            ]),
        ]
        
        self.default_responses = [
            "I'm not sure I understand. Can you rephrase that?",
            "Interesting! Tell me more.",
            "I see. What else would you like to know?",
            "That's a good question! I'm still learning.",
            "Hmm, I'm not quite sure about that. Try asking something else!"
        ]
    
    def get_response(self, user_input):
        """Get a response based on user input using pattern matching."""
        # Check each pattern
        for pattern, responses in self.patterns:
            if pattern.search(user_input):
                # Handle special case for time
                if responses == 'time':
                    return random.choice([
                        f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                        f"It's {datetime.now().strftime('%I:%M %p')} right now"
                    ])
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
