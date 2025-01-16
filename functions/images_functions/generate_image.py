from PIL import Image, ImageDraw

# Create a new blank image
width, height = 199, 107  # Matching dimensions of the example
base_color = (205, 133, 63)  # Approximation of the lighter brown color

# Create the base layer
game_texture = Image.new("RGB", (width, height), base_color)
draw = ImageDraw.Draw(game_texture)

# Add the darker section (lower part)
darker_color = (184, 115, 51)  # Approximation of the darker brown color
draw.rectangle([(0, height // 2), (width, height)], fill=darker_color)

# Add the subtle dividing line
line_color = (153, 76, 0)  # Even darker brown for the line
line_thickness = 2  # Thickness of the dividing line
line_y = height // 2
draw.rectangle([(0, line_y - line_thickness), (width, line_y + line_thickness)], fill=line_color)

# Save the image
output_game_texture_path = 'data/game_texture.png'
game_texture.save(output_game_texture_path)
output_game_texture_path
