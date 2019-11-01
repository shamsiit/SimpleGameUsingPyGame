# SimpleGameUsingPyGame

This is an basic game written by python language with help of [pygame](https://www.pygame.org/)

## Gameplay

- press `q` to quit the game.
- press  `spacebar` to shoot the planet !



## Dev notes 

#### functions used in this project

- To set screen size:

  ```python
  pygame.display.set_mode(screensize)
  ```

  change value of *screensize* 

  

- to load image in a variable:

  ```python
  pygame.image.load("imagename") 
  ```

  change value of *imagename*

- to identify key pressed, look through:

  ```python
  pygame.key.get_pressed() 
  ```

- for updating the screen

  ```python
  pygame.display.update()
  ```

- for setting the image positions in game screen:

  ```python
  screen.blit(image_name,screen_position) 
  ```

  - different screen positions:
    - left top corner is (0,0) coordinate
    - horizontal axis is x axis
    - top to bottom is y axis

 