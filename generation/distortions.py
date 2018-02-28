from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps
import numpy as np

def blur(coordinates, factor, fingerprint):
    mask = Image.new('L', fingerprint.size)

    ImageDraw.Draw(mask).ellipse(coordinates, 255)

    return Image.composite(fingerprint.filter(ImageFilter.GaussianBlur(factor)),
                           fingerprint,
                           mask.filter(ImageFilter.GaussianBlur(25)))

def brightness(coordinates, factor, fingerprint):
    mask = Image.new('L', fingerprint.size)

    ImageDraw.Draw(mask).ellipse(coordinates, 255)

    return Image.composite(ImageEnhance.Brightness(fingerprint).enhance(factor),
                           fingerprint,
                           ImageChops.multiply(mask.filter(ImageFilter.GaussianBlur(25)), ImageChops.invert(fingerprint)))

def composite(background, fingerprint):
    return Image.composite(ImageOps.fit(background.convert('RGB'), fingerprint.size, centering = np.random.rand(2)),
                           fingerprint.convert('RGB'),
                           fingerprint)

def contrast(coordinates, factor, fingerprint):
    mask = Image.new('L', fingerprint.size)

    ImageDraw.Draw(mask).ellipse(coordinates, 255)

    return Image.composite(ImageEnhance.Contrast(fingerprint).enhance(1 / factor),
                           fingerprint,
                           ImageChops.multiply(mask.filter(ImageFilter.GaussianBlur(25)), ImageChops.invert(fingerprint)))

def line(coordinates, factor, fingerprint):
    fingerprint_ = fingerprint.copy()

    ImageDraw.Draw(fingerprint_).line(coordinates, 255, int(factor))

    return fingerprint_

def resolution(coordinates, factor, fingerprint):
    mask = Image.new('L', fingerprint.size)

    ImageDraw.Draw(mask).ellipse(coordinates, 255)

    return Image.composite(fingerprint.resize([int(i / factor) for i in fingerprint.size]).resize(fingerprint.size),
                           fingerprint,
                           mask.filter(ImageFilter.GaussianBlur(25)))

def rotation(coordinates, factor, fingerprint):
    background = Image.new('L', fingerprint.size, 255) 
    mask = Image.new('L', fingerprint.size)

    ImageDraw.Draw(mask).ellipse(coordinates, 255)

    return Image.composite(Image.composite(fingerprint.rotate(factor), background, background.rotate(factor)),
                           fingerprint,
                           mask.filter(ImageFilter.GaussianBlur(25)))