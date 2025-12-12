#!/usr/bin/env python3
import sys
from openai import OpenAI

client = OpenAI()

prompts = {
    "kort og præcis": "Du er en hjælpsom assistent, der altid svarer kort og præcist.",
    "venlig og sjov": "Du er venlig, sjov og bruger emojis i dine svar.",
    "lærerig": "Du forklarer alt grundigt, som om læseren er nybegynder."
}

print("Vælg system prompt:")
for i, key in enumerate(prompts.keys(), 1):
    print(f"{i}. {key}")

choice = input("Indtast nummer: ")
selected_prompt = list(prompts.values())[int(choice) - 1]

history = [{"role": "system", "content": selected_prompt}]


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

            assistant = response.choices[0].message.content
            print(f"\n{assistant}\n")

            history.append({"role": "assistant", "content": assistant})

        except KeyboardInterrupt:
            print("\nFarvel 👋")
            sys.exit(0)

if __name__ == "__main__":
    chat()
