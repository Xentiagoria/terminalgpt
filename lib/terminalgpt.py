#!/usr/bin/env python3
import sys
from openai import OpenAI

client = OpenAI()

def chat():
    print("TerminalGPT – interaktiv CLI-chat (CTRL+C for at afslutte)\n")

    history = []

    while True:
        try:
            user_input = input("> ")

            history.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=history
            )

            assistant = response.choices[0].message["content"]
            print(f"\n{assistant}\n")

            history.append({"role": "assistant", "content": assistant})

        except KeyboardInterrupt:
            print("\nFarvel 👋")
            sys.exit(0)

if __name__ == "__main__":
    chat()
