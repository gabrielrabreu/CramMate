from pathlib import Path

from crampy.running import Transformer, Settings


def run():
    settings = Settings()
    settings.convert_extension = "html"
    settings.convert_mode = "practice_test"

    source = Path("C:\\Development\\CramPy\\files\\matematica_facil.json")

    Transformer(settings).transform(source)


if __name__ == "__main__":
    print("CramPy!")
    run()
