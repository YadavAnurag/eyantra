import cv2
import numpy as np
import os

def partA():

	def performImageTask(csvFile, rootDir, image):
		stats = []
		img = cv2.imread(rootDir+image)
		
		name = image.split('.')[0]
		stats.append(name)

		height,width,channel = img.shape
		stats.append(height)
		stats.append(width)
		stats.append(channel)


		pixel_b, pixel_g, pixel_r = img[height//2, width//2]
		stats.append(pixel_b)
		stats.append(pixel_g)
		stats.append(pixel_r)


		# writing imageProperties to csvFile
		stats = list(map(str, stats))
		imageStats = ','.join(stats)
		csvFile.write(imageStats+'\n')


	def mainPartA():
		imagesPath = '../Images/'

		with open('../Generated/stats.csv', mode='a') as csvFile:
			for rootDir,_,images in os.walk(imagesPath):
				for image in images:
					performImageTask(csvFile, rootDir, image)

	mainPartA()				

def partB():
    catImagePath = '../Images/cat.jpg'
    generatedPath = '../Generated/cat_red.jpg'


    img = cv2.imread(catImagePath)
    
    redCat = img.copy()
    redCat[..., :2] = 0
    
    cv2.imwrite(filename=generatedPath, img=redCat)


def partC():
    flowersImagePath = '../Images/flowers.jpg'
    generatedPath = '../Generated/flowers_alpha.png'

    img = cv2.imread(flowersImagePath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    img[..., 3] = 128
    
    cv2.imwrite(filename=generatedPath, img=img)


def partD():
    imgPath = "../Images/horse.jpg"
    generatedPath = "../Generated/horse_gray.jpg"
    img = cv2.imread(imgPath)
    I = .3 * img[..., 2] + .59 * img[..., 1] + .11 * img[..., 0]
    cv2.imwrite(generatedPath, I)


partA()
partB()
partC()
partD()