import arcade 
import arcade.gui
import random
from algos.sort.bubble import bubble_sort
from algos.sort.insertion import insertion_sort
from algos.sort.selection import selection_sort
from algos.sort.merge import merge_sort
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Algo Visualizer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class AlgoVisualizer(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.array = []
        self.array_color = []
        self.sorting_done = False
        self.delay_counter = 0
        self.sorting_speed = 10
        self.start_sorting = False
        self.sorting_algorithm = "bubble"
        # self.merge_sort_state = None  # Initialize as None
        self.volume = 0.1
        self.swap_sound = arcade.load_sound(":resources:sounds/fall3.wav")
        self.done_sound = arcade.load_sound(":resources:sounds/coin1.wav")

    def setup(self):
        self.array = [i for i in range(1, 50)]
        self.array_colors = [arcade.color.BLUE for _ in self.array]

        random.shuffle(self.array)

    def on_draw(self):
        arcade.start_render()

        self.button() 

        bar_width = SCREEN_WIDTH / len(self.array)
        for i, value in enumerate(self.array):
            color = self.array_colors[i]
            arcade.draw_rectangle_filled(
                (i * 1) * bar_width, value * 5,
                bar_width - 2,
                value * 10,
                color
            )

        

    def update(self, delta_time):
        if self.start_sorting and not self.sorting_done:
            self.delay_counter += 1
            if self.delay_counter >= self.sorting_speed:
                #bubble_sort(self.array)
                self.sort_step()
                self.delay_counter = 0

    def button(self):
        arcade.gui.UIFlatButton(0,0, 100, 50, "Start")

        
        
    def sort_step(self):
        if self.sorting_algorithm == "bubble":
            bubble_sort(self.array, self.swap_sound, self.volume)
        elif self.sorting_algorithm == "insertion":
            insertion_sort(self.array, self.swap_sound, self.volume)
        elif self.sorting_algorithm == "merge":
            merge_sort(self.array)
        elif self.sorting_algorithm == "selection":
            selection_sort(self.array, self.swap_sound, self.volume)
        
        

            

    def on_key_press(self, key, modififers):
        print(f"Key preesed {key}")
        if key == arcade.key.R:
            self.setup()
            self.start_sorting = False
            self.sorting_done = False
        elif key == arcade.key.B or key == 98:  # Bubble sort
            self.sorting_algorithm = "bubble"
            print("Selected algorithm: Bubble Sort")
            self.start_sorting = True
        elif key == arcade.key.I:  # Insertion sort
            self.sorting_algorithm = "insertion"
            print("Selected algorithm: Insertion Sort")
            self.start_sorting = True
        elif key == arcade.key.M:  # merge sort
            self.sorting_algorithm = "merge"
            print("Selected algorithm: merge Sort")
            self.start_sorting = True
        elif key == arcade.key.S:  # selection sort
            self.sorting_algorithm = "selection"
            print("Selected algorithm: selection Sort")
            self.start_sorting = True
        elif key == arcade.key.UP:
            self.sorting_speed = max(1, self.sorting_speed - 1)
        elif key == arcade.key.DOWN:
            self.sorting_speed = max(10, self.sorting_speed + 1)


def main():
    window = AlgoVisualizer()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()