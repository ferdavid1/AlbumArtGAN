import PIL
import os 

def scale(filename):
	img = PIL.open(filename)
	img.scale(1111)
	return scaled, filename
def write(scaled, filename):
	img.save('scaled_results'+filename)
if __name__ == '__main__':
	os.chdir('images/')
	for img in os.listdir('results/'):
		scaled, filename = scale('results/' + str(img))
		write(scaled, filename)
