from PIL import Image
from rich import console
from rich.console import Console
import argparse


class TextImage:
    def __init__(self, file, width=120, double=False):
        self.file = file
        self.width = width
        self.double = double

    def convert(self):
        img = Image.open(self.file)
        w, h = img.size
        img = img.resize((self.width, self.width * h // w))
        console = Console()
        p = "##" if self.double else "#"
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                r, g, b = img.getpixel((x, y))
                console.print(p, style=f"rgb({r},{g},{b}) on rgb({r},{g},{b})", end="")
            console.print("")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="text-image")
    parser.add_argument("file", type=str)
    parser.add_argument("--width", type=int, default=120)
    parser.add_argument("-2", action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args()
    text_image = TextImage(args.file, args.width, getattr(args, "2"))
    text_image.convert()
