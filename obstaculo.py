from typing import Any
from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale

class Obstaculo(Sprite):
    image = scale(load('fire.png'), (100, 200))
    rect = image.get_rect(center=(1500, 350))


    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.x -= 10
        if self.rect.x == -300:
            self.rect.x = 1500