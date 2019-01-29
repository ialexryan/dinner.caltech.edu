from PIL import Image

im = Image.open("menu.png")
pix = im.load()

width, height = im.size

# Okay, first we're going to find out where the top of the grid is.
# We're going to do that by choosing a column of pixels about 1/3 of
# the way in from the left side of the document, and then iterating
# down that column of pixels until we see something that isn't white.
top_of_grid = -1
for i in range(0, height):
  val = pix[(width/3), i]
  if val[0] < 255 and val[1] < 255:
    top_of_grid = i
    break
assert(top_of_grid != -1)
# print "Found the top of the grid at row " + str(top_of_grid)

# Now we're going to find the bottom of the grid. It's the same idea,
# but a little trickier because we have to ignore the two rows of
# "legend" information at the bottom of the page.
bottom_of_legend = False
top_of_legend = False
bottom_of_grid = -1
for i in reversed(range(0, height)):
  val = pix[(width/4), i] # one cell in the legend is white at 1/3 over, so that was messing up
  if not bottom_of_legend:
    if val[0] < 255 and val[1] < 255:
      bottom_of_legend = True
  elif not top_of_legend:
    if val[0] == 255 and val[1] == 255:
      top_of_legend = True
  else:
    if val[0] < 255 and val[1] < 255:
      bottom_of_grid = i
      break
assert(bottom_of_legend)
assert(top_of_legend)
assert(bottom_of_grid != -1)
# print "Found the bottom of the grid at row " + str(bottom_of_grid)

# Now that we know where the top of the grid is, we're going to iterate
# over the row of pixels just under it and identify all the column boundaries.
boundaries = []
prev_val = pix[0, top_of_grid + 3]
for i in range(1, width):
	val = pix[i, top_of_grid + 3]
	if val != prev_val and prev_val == (0,0,0):
		boundaries.append(i)
	prev_val = val
assert(len(boundaries) == 7)
assert(width/3 not in boundaries)
# print "We found column boundaries at " + str(boundaries)

Monday = im.crop((boundaries[1], top_of_grid, boundaries[2], bottom_of_grid))
Tuesday = im.crop((boundaries[2], top_of_grid, boundaries[3], bottom_of_grid))
Wednesday = im.crop((boundaries[3], top_of_grid, boundaries[4], bottom_of_grid))
Thursday = im.crop((boundaries[4], top_of_grid, boundaries[5], bottom_of_grid))
Friday = im.crop((boundaries[5], top_of_grid, boundaries[6], bottom_of_grid))
Monday.save("Monday.png", "PNG")
Tuesday.save("Tuesday.png", "PNG")
Wednesday.save("Wednesday.png", "PNG")
Thursday.save("Thursday.png", "PNG")
Friday.save("Friday.png", "PNG")
