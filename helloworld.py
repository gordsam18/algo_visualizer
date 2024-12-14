import arcade

#constatnts 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Algo Visulizer"
PLAYER_MOVEMENT_SPEED = 5

CHARACTER_SCALING = 1
TITLE_SCALING = 0.5 

class MyGame( arcade.Window):
    
    def __init__(self):
      # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.

        #Scene object 
        self.scene =None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        #Initialize Scene
        self.scene = arcade.Scene()

        
        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        #Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0,1250,64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TITLE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordiantes in coordinate_list:
            # add a create on the fround 
            wall = arcade.Sprite( ":resources:images/tiles/boxCrate_double.png", TITLE_SCALING)
            wall.position = coordiantes
            self.scene.add_sprite("Walls", wall)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls")
        )


    def on_draw(self): 
        """Render the screen."""

        self.clear()
        # code to draw the screen goes here

        #Draw the sprites
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is preessed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED    
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED    
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED 

    def on_key_release(self, key, modifiers):
        """Called when key is released. """   
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        self.physics_engine.update()



def main():
    window = MyGame()
    window.setup()
    window.run()

if __name__ =="__main__":
    main()
