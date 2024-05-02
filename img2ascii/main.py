from PIL import Image
import argparse

parser = argparse.ArgumentParser(
    prog='img2ascii',
    description='Converts images into ascii'
)
parser.add_argument('image')
parser.add_argument('-s', '--size', help='changes the size using multiplication', default=1)

args = parser.parse_args()

with Image.open(args.image) as im:
    sz = im.size
    im = im.resize((round(sz[0]*float(args.size)), round(sz[1]*float(args.size))))
    sz = im.size
    cols = []
    for ii in range(round(sz[1]*0.5)):
        rows = []
        for i in range(sz[0]):
            try:
                c1 = im.getpixel((i, ii*2))
            except IndexError as e:
                c1 = None
            try:
                c2 = im.getpixel((i, ii*2+1))
            except IndexError as e:
                c2 = None
            rows.append((c1, c2))
        cols.append(rows)
    for col in range(len(cols)):
        rows = cols[col]
        for row in range(len(cols[col])):
            if not cols[col][row][0] == None:
                r, g, b = cols[col][row][0]
            if not cols[col][row][1] == None:
                r2, g2, b2 = cols[col][row][1]
            # ▀ is used for square symbol
            print(f'\x1b[38;2;{r};{g};{b}m\x1b[48;2;{r2};{g2};{b2}m▀\x1b[0m', end='')
        print('')
