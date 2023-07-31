def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

def main():
    text = input("Yell something at a mountain: ")
    print(echo(text))

if __name__ == "__main__":
    main()