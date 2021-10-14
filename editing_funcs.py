import skimage.transform
from scanning import *


class Editing:

    @staticmethod
    def f000(img):
        new_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return new_img

    @staticmethod
    def f001(img):
        new_img = Editing.f000(img)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f002(img):
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f003(img):
        rescale_factor = 0.75
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f004(img):
        rescale_factor = 1.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f005(img):
        rescale_factor = 2.0
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f006(img):
        rescale_factor = 2.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        return new_img

    @staticmethod
    def f007(img):
        rescale_factor = 0.75
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f008(img):
        rescale_factor = 1.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f009(img):
        rescale_factor = 2.0
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f010(img):
        rescale_factor = 2.5
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f011(img):
        rescale_factor = 0.75
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f012(img):
        rescale_factor = 1.5
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f013(img):
        rescale_factor = 2.0
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f014(img):
        rescale_factor = 2.5
        kernel_size = 3
        new_img = Editing.f000(img)
        new_img = np.uint8(
            skimage.transform.rescale(new_img, (rescale_factor, rescale_factor), multichannel=False,
                                      preserve_range=True))
        new_img = cv.GaussianBlur(new_img, (kernel_size, kernel_size), 0)
        new_img = cv.adaptiveThreshold(new_img, WHITE, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,
                                       THRESHOLD_KERNEL_SIZE, THRESHOLD_BIAS)
        return new_img

    @staticmethod
    def f015(img):
        new_img = Editing.f001(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f016(img):
        new_img = Editing.f007(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f017(img):
        new_img = Editing.f008(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f018(img):
        new_img = Editing.f009(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f019(img):
        new_img = Editing.f010(img)
        new_img = dilation(new_img)
        return new_img

    @staticmethod
    def f020(img):
        new_img = Editing.f001(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f021(img):
        new_img = Editing.f007(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f022(img):
        new_img = Editing.f008(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f023(img):
        new_img = Editing.f009(img)
        new_img = erosion(new_img)
        return new_img

    @staticmethod
    def f024(img):
        new_img = Editing.f010(img)
        new_img = erosion(new_img)
        return new_img
