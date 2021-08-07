from PIL import Image

# Img resize: 
# ant_size = 0.01
# ant_img = Image.open('imgs/ant.png')
# orig_ant_height, orig_ant_width = ant_img.size
# ant_img = ant_img.resize((round(orig_ant_width*ant_size), 
#                 round(orig_ant_width*ant_size)))
# ant_img.save('imgs/small_ant.png')


# for spin in [45, 90, 135, 180, 225, 270, 315]:
#     ant_img = ant_img.rotate(-45)
#     ant_img.save(f'imgs/small_ant{spin}.png')

food_img = Image.open('imgs/sugar.png')

height, width = food_img.size

food_img = food_img.resize((round(height*0.01), round(height*0.01)))
food_img.save('imgs/sugar_small.png')