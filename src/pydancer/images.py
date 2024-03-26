from .constants import *
from .image_functions import *

# dancer images
dancer_image = load_image("../images/dancer.png")
dancer_image = scale_image(dancer_image, DANCER_WIDTH, DANCER_HEIGHT)

# purple end area image
end_area_image = load_image("../images/end_area.png")
end_area_image = scale_image(end_area_image, SCREEN_WIDTH, SCREEN_HEIGHT * .2)
