import os
import numpy as np
from PIL import Image
import multiprocessing
import time

mainImg = Image.open("ob.jpg").convert("RGB")
pixels = mainImg.load()
cols, rows = mainImg.size

tSize = 20
s = tSize * tSize
path = r'C:\Users\wikto\Desktop\bigDataProjt\images_0003'
divisor = multiprocessing.cpu_count()

avgRgbVals = []
files = []
rgb = []

for subDir in os.listdir(path):
    full_subDir_path = os.path.join(path, subDir)
    if os.path.isdir(full_subDir_path):
        for file in os.listdir(full_subDir_path):
            full_file_path = os.path.join(full_subDir_path, file)
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                files.append(full_file_path)

packsOfImages = np.array_split(files, divisor)
packsOfImages = [list(pack) for pack in packsOfImages]

def processImg(packs):
    result = []
    for img in packs:
        try:
            with Image.open(img).convert("RGB") as rgbImg:
                npImg = np.array(rgbImg)
                avgRgb = np.mean(npImg, axis=(0, 1))
                result.append(avgRgb)
        except Exception as e:
            print(f"Błąd przy przetwarzaniu obrazu {img}: {e}")
    return result

def closest_image(pixel_rgb, avg_rgb_vals, k):
    diffs = np.array(avg_rgb_vals) - np.array(pixel_rgb[k])
    dists = np.sqrt(np.sum(diffs**2, axis=1))
    minDist = np.min(dists)
    minIdxs = np.where(dists == minDist)
    return np.random.choice(minIdxs[0])

def returnPixels(rgbList):
    for i in range(cols // tSize):
        for j in range(rows // tSize):
            r, g, b = 0, 0, 0
            for x in range(tSize):
                for y in range(tSize):
                    rPx, gPx, bPx = pixels[i * tSize + x, j * tSize + y]
                    r += rPx
                    g += gPx
                    b += bPx
            r = int(r / s)
            g = int(g / s)
            b = int(b / s)
            rgbList.append([r, g, b])
    return rgbList

def makeMossaic(indexTab):
    final_image = Image.new("RGB", (cols, rows))
    k = 0
    for i in range(cols // tSize):
        for j in range(rows // tSize):
            idx = indexTab[k]
            img_path = files[idx]
            try:
                with Image.open(img_path) as tile:
                    tile = tile.resize((tSize, tSize))
                    final_image.paste(tile, (i * tSize, j * tSize))
            except Exception as e:
                print(f"Błąd przy wklejaniu obrazka {img_path}: {e}")
            k += 1
    final_image.save(f"mosaic_{tSize}.png")
    print("Mozaika zapisana!")

if __name__ == "__main__":
    start = time.time()


    pool = multiprocessing.Pool()
    results = pool.map(processImg, packsOfImages)
    pool.close()
    pool.join()

    for result in results:
        avgRgbVals.extend(result)

    print(f"Łącznie przetworzonych zdjęć: {len(avgRgbVals)}")

    rgb = returnPixels([])


    args_ = [(rgb, avgRgbVals, k) for k in range(len(rgb))]

    
    chunksize_ = len(args_) // (divisor * 8)
    poolForImgProcessing = multiprocessing.Pool()
    res = poolForImgProcessing.starmap(closest_image, args_, chunksize=chunksize_)
    poolForImgProcessing.close()    
    poolForImgProcessing.join()

    makeMossaic(res)

    end = time.time()
    time_ = round(end - start,2)
    print(f"Czas trwania programu: {time_} sekundy")
