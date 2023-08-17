import turtle

from Hirst_Painting_Generator import Generator

my_generator = Generator()

consent = "y"
while consent != "n":
    consent = input("Press 'y' to generate a Hirst Painting or 'n' to exit: ")
    if consent == "n":
        break
    elif consent == "y":
        response = input("Do you wish to provide an image to be sampled for colors? (y/n): ")
    else:
        continue
    if response == "y":
        path = input(
            r"Please paste the image path (eg. 'C:\Users\Nitesh\Documents\image.jpg'): ")
        no_of_colors = input("Please type the number of colors you want to extract from the image. (default is 30): ")
        if no_of_colors is None:
            no_of_colors = 30
        no_of_colors = int(no_of_colors)
        list_of_rgb = my_generator.extract_color_palette(path=path, number_of_colors=no_of_colors)
        my_generator.generate_painting(list_of_rgb=list_of_rgb)
    elif response == 'n':
        my_generator.generate_painting(list_of_rgb=None)

        should_randomize = input("Randomize colors? (y/n): ")
        # turtle.bye()
        while should_randomize == "y":
            my_generator.generate_painting(list_of_rgb=None)
            should_randomize = input("Randomize colors? (y/n): ")
            # turtle.bye()
            if should_randomize == "n":
                break
    else:
        continue
