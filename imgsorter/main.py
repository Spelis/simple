import argparse
import os
from PIL import Image


def filterlist(orglist, substr):
    return [item for item in orglist if item.endswith(substr)]


parser = argparse.ArgumentParser('imgsorter', description='sorts images into separate directories by average color')
parser.add_argument('directory')
parser.add_argument('filetype')
args = parser.parse_args()
files = filterlist(os.listdir(args.directory), args.filetype)
for i in files:
    with Image.open(os.path.join(args.directory, i)) as img:
        img.convert('RGB')
        img.resize((32, 32))
        pix = img.load()
        red_sum = 0
        green_sum = 0
        blue_sum = 0
        total_pixels = img.size[0] * img.size[1]
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                # Add the RGB values of the current pixel to the sums
                red_sum += pix[x, y][0]
                green_sum += pix[x, y][1]
                blue_sum += pix[x, y][2]
        avg = (red_sum // total_pixels, green_sum // total_pixels, blue_sum // total_pixels)
        r, g, b = avg
        r = round((r / 255) * 32)
        g = round((g / 255) * 32)
        b = round((b / 255) * 32)
        c = f"color: ({r*8}, {g*8}, {b*8})"
        if not os.path.exists(os.path.join(args.directory, c)):
            os.mkdir(os.path.join(args.directory, c))
        os.rename(os.path.join(args.directory, i), os.path.join(args.directory, str(c), i))
