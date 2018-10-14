from PIL import Image, ImageEnhance
import os 

def scale(filename, outfilename):
	img = Image.open(filename)
	img = img.resize((1400,1400), Image.ANTIALIAS)
	contrast = ImageEnhance.Contrast(img) # enhance contrast
	contrast.enhance(5).save('scaled_results/' + outfilename)
if __name__ == '__main__':
	os.chdir('images/lr-0002') # change lr-00XXX to whichever trial run you're on
	for imgname in os.listdir('results/'):
		scaled = scale('results/' + imgname, imgname.strip('.png') + '_scaled.png')
		print("Scaled: ", imgname)