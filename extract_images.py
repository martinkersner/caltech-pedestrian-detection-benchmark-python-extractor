import os
import sys
import glob
import struct

def main():
    input_dir  = sys.argv[1]
    output_dir = sys.argv[2]

    # walk through all all 'sets' of images
    for x in os.walk(input_dir):
        extract(os.path.join(input_dir, x[0]), output_dir)

def detect_format(image_format):
    if image_format == 100 or image_format == 200:
        return ".raw"
    elif image_format == 101:
        return ".brgb8"
    elif image_format == 102 or image_format == 201:
        return ".jpg"
    elif image_format == 103:
        return ".jbrgb"
    elif image_format == 1 or image_format == 2:
        return ".png"
    else:
        print "Invalid extension format " + image_format
        return None

def write_img(path, img_name, img_data):
    with open(os.path.join(path,img_name), "wb") as f:
        f.write(bytearray(img_data))

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_output_dir(input_dir, output_dir):
    create_dir(output_dir) 

def extract(input_dir, output_dir):
    # test input dir -> stop
    # test output dir -> create
    SKIP = 28 + 8 + 512

    print input_dir, "input directory \n \n \n"

    for filename in glob.glob(os.path.join(input_dir, "*.seq")):
        print filename

        im_set = input_dir[-5:]

        create_dir(os.path.join(output_dir, im_set))

        with open(filename, "rb") as f:
            f.seek(SKIP)

            header_info = ["width", "height", "imageBitDepth", 
                           "imageBitDepthReal", "imageSizeBytes", 
                           "imageFormat", "numFrames"]
            header = {}

            for attr in header_info:
                header[attr] = struct.unpack('I', f.read(4))[0] 

            f.read(4) # skip 4 bytes

            header["trueImageSize"] = struct.unpack('I', f.read(4))[0] 
            header["fps"] = struct.unpack('d', f.read(8))[0] 

            print header

            ext = detect_format(header["imageFormat"])

            f.seek(432, 1) # skip to image data
            for img_id in range(header["numFrames"]):
                img_size = struct.unpack('I', f.read(4))[0] 

                img_data = f.read(img_size)
                img_name = str(img_id) + ext
                write_img(os.path.join(output_dir,im_set), img_name, img_data)

                f.seek(12, 1) # skip to next image

if __name__ == "__main__":
    main()
