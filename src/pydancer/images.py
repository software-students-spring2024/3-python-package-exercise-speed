from .constants import *
from .image_functions import *

# dancer images
dancer_image_girl = load_image("../static/images/dancer.png")
dancer_image_girl = scale_image(dancer_image_girl, DANCER_WIDTH, DANCER_HEIGHT)

dancer_image_boy = load_image("../static/images/dance.png")
dancer_image_boy = scale_image(dancer_image_boy, DANCER_WIDTH, DANCER_HEIGHT)

# purple end area image
end_area_image = load_image("../static/images/end_area.png")
end_area_image = scale_image(end_area_image, SCREEN_WIDTH, SCREEN_HEIGHT * .15)

