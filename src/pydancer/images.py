from .constants import *
from .image_functions import *

# glow arrows:
left_glow_arrow_image = load_image("../static/images/left_arrow_glow.png")
left_glow_arrow_image = scale_image(left_glow_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)

right_glow_arrow_image = load_image("../static/images/right_arrow_glow.png")
right_glow_arrow_image = scale_image(right_glow_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)

up_glow_arrow_image = load_image("../static/images/up_arrow_glow.png")
up_glow_arrow_image = scale_image(up_glow_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)

down_glow_arrow_image = load_image("../static/images/down_arrow_glow.png")
down_glow_arrow_image = scale_image(down_glow_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)

# dancer images
dancer_image = load_image("../static/images/dancer.png")
dancer_image = scale_image(dancer_image, DANCER_WIDTH, DANCER_HEIGHT)

# purple end area image
end_area_image = load_image("../static/images/end_area.png")
end_area_image = scale_image(end_area_image, SCREEN_WIDTH, SCREEN_HEIGHT * .15)

