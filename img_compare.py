from PIL import Image
import numpy as np
import sys


class ImageCompare(object):
    def __init__(self, image_one, image_two):
        self.image_one = image_one
        self.image_two = image_two

    def compare(self):
        image1 = Image.open(self.image_one)
        image2 = Image.open(self.image_two)

        # Convert img to numpy array
        array1 = np.array(image1)
        array2 = np.array(image2)

        # fit image to largest shape
        if array1.shape != array2.shape:
            if array1.shape > array2.shape:
                array2 = np.resize(array2, array1.shape)
            else:
                array1 = np.resize(array1, array2.shape)

        mse = ((array1 - array2) ** 2).mean(axis=None) # Mean squared Error

        prob_change = mse / 255 # 255 is the max value of a pixel

        print("Rate of Change: {:.2f}%".format(prob_change * 100))

        difference = array1 - array2
        difference[difference != 0] = 255
        diff_image = Image.fromarray(difference.astype('uint8'))
        diff_image.show()


if __name__ == '__main__':
    image1 = sys.argv[1]
    image2 = sys.argv[2]
    ic = ImageCompare(image1, image2)
    ic.compare()
