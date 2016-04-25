#!/usr/bin/python

from PIL import Image

im = Image.open("menu.png")
pix = im.load()

width, height = im.size

boundaries = []

for i in range(0, width):
	val = pix[i, 160]
	if val[0] < 255 and val[1] < 255:
		if (i - 1) in boundaries:
			boundaries.remove(i - 1)
		boundaries.append(i)

Monday = im.crop((boundaries[1], 150, boundaries[2], height-200))
Tuesday = im.crop((boundaries[2], 150, boundaries[3], height-200))
Wednesday = im.crop((boundaries[3], 150, boundaries[4], height-200))
Thursday = im.crop((boundaries[4], 150, boundaries[5], height-200))
Friday = im.crop((boundaries[5], 150, boundaries[6], height-200))
Monday.save("Monday.png", "PNG")
Tuesday.save("Tuesday.png", "PNG")
Wednesday.save("Wednesday.png", "PNG")
Thursday.save("Thursday.png", "PNG")
Friday.save("Friday.png", "PNG")
