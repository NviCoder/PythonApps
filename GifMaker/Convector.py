import imageio
import os 

clip = os.path.abspath('Dwayne_Johnson.mp4')

def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps = fps)
    numbersOfFrames = 1

    for frames in reader:    
        writer.append_data(frames)
        print(f'Frame Number {numbersOfFrames} \n {frames}')
        numbersOfFrames = numbersOfFrames + 1
    print('Done!') 
    writer.close()

gifMaker(clip,'.gif')  
