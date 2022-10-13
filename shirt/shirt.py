import sys
import os
from PIL import Image, ImageOps
from sqlalchemy import over

ACCEPTED_FORMATS = [".jpeg", ".jpg", ".png"]


def main():
    check_input(sys.argv)

    input_path, output_path = sys.argv[1:]
    overlay_shirt(input_path, output_path)


def check_input(args):
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")

    _, input_extension = os.path.splitext(args[1])
    _, out_extension = os.path.splitext(args[2])

    if input_extension != out_extension:
        sys.exit("Input and output have different extensions")

    if not input_extension in ACCEPTED_FORMATS:
        sys.exit("Invalid input")

    try:
        open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("Input does not exist")


def overlay_shirt(input_path, output_path):
    shirt = Image.open("shirt.png")
    input_image = Image.open(input_path)
    resized_input_image = ImageOps.fit(input_image, shirt.size)
    resized_input_image.paste(shirt, shirt)
    resized_input_image.save(output_path)


if __name__ == "__main__":
    main()
