import imageio

filenames = ['barney_1.png', 'barney_2.png']
images = []

for filename in filenames:
  images.append(imageio.imread(filename))

imageio.mimsave('barney.gif', images, duration = 0.5)

