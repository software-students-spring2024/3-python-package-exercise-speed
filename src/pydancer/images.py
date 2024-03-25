from .constants import *
from .image_functions import *

glow_arrow_image = load_image("../images/left_arrow_glow.png")
glow_arrow_image = scale_image(glow_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)

dancer_image = load_image("../images/dancer.png")
dancer_image = scale_image(dancer_image, DANCER_WIDTH, DANCER_HEIGHT)

end_area_image = load_image("../images/end_area.png")
end_area_image = scale_image(end_area_image, SCREEN_WIDTH, SCREEN_HEIGHT * .2)
