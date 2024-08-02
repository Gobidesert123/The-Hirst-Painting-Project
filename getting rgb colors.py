
import colorgram
# Getting a list of rgb colors as tuples in the (r, g, b) format
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

# print(rgb_colors)