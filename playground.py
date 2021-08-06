from PIL import Image

ant_size = 0.1
ant_img = Image.open('imgs/ant.png')
orig_ant_height, orig_ant_width = ant_img.size
ant_img.resize((round(orig_ant_width*ant_size), 
                round(orig_ant_width*ant_size)))


ant_img.save('small_ant.png')
