from PIL import Image
import os 

def scale(filename, outfilename):
	img = Image.open(filename)
	img = img.resize((1400,1400), Image.ANTIALIAS)
	img.save('scaled_results/' + outfilename)
	return img

if __name__ == '__main__':
	os.chdir('images/lr-0002') # change lr-0002 to whichever trial run you're on
	for imgname in os.listdir('results/'):
		scaled = scale('results/' + imgname, imgname.strip('.png') + '_scaled.png')
		print("Scaled: ", imgname)