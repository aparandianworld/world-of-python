#!/usr/bin/env python3


class WordSet:
    _replace_puncs = ["!", "?", ".", ",", ";", ":", '"', "'", "-"]

    def __init__(self):
        self.words = set()

    def add_text(self, text):
        text = WordSet.clean_text(text) # text = self.clean_text(text)
        for word in text.split():
            self.words.add(word)

    @staticmethod
    def clean_text(text):
        for punc in WordSet._replace_puncs:
            text = text.replace(punc, "")
        return text.lower()


def main():
    ws = WordSet()
    ws.add_text(
        "On November 24, 2025, the AI landscape buzzed with pivotal developments underscoring massive investments and geopolitical maneuvers, as Alphabet's Google surged 5% in stock value after clinching a landmark NATO cloud and AI contract leveraging its custom TPU chips, bolstering its $3.8 trillion market cap amid bullish signals like Berkshire Hathaway's stake and robust earnings. Meanwhile, Tesla advanced its autonomous driving ambitions by hiring an AI Engineer focused on reinforcement learning and model distillation to optimize Full Self-Driving software for hardware-limited vehicles like those with HW3 chips, signaling broader accessibility for its fleet. Intel's shares hovered around $34, buoyed by a $2 billion SoftBank infusion positioning it as a CHIPS Act-backed AI powerhouse, while Nokia announced a $4 billion U.S. AI investment; however, concerns mounted over governments ceding AI oversight to Big Tech under policies like a 10-year U.S. state regulation ban, potentially stifling ethical innovation. These stories highlight AI's accelerating integration into defense, mobility, and infrastructure, tempered by calls for democratized governance to counter tech giants' dominance."
    )
    print(ws.words)


if __name__ == "__main__":
    main()
