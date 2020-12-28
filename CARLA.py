import os
from skimage import io
from tqdm.auto import tqdm
from env import KITTI_DATASET_PATH
import numpy as np


def main():
    path = '/home/yifu/Downloads/000020.png'
    img = io.imread(path)
    output = np.zeros_like(img[:,:,1])
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            R = img[i,j,0]
            G = img[i,j,1]
            B = img[i,j,2]
            normalized = (R + G * 256 + B * 256 * 256) / (256 * 256 * 256 - 1)
            in_meters = 1000 * normalized
            output[i,j] = in_meters
    io.imsave('/home/yifu/workspace/test/test.png',output)
    # normalized = (R + G * 256 + B * 256 * 256) / (256 * 256 * 256 - 1)
    # in_meters = 1000 * normalized


if __name__ == '__main__':
    main()
    '''
    if not os.path.exists(KITTI_NORMALS_PATH):
        os.mkdir(KITTI_NORMALS_PATH)

    processing_args = []
    for split in ['train', 'val']:
        date_folder_list = sorted(os.listdir(os.path.join(KITTI_GT_PATH, split))) # list of 2011_XX_XX_drive_XXXX_sync
        
        for date_folder in date_folder_list:
            sub_path_to_date_folder = os.path.join(split, date_folder, 'proj_depth', 'groundtruth')
            gt_path = os.path.join(KITTI_GT_PATH, sub_path_to_date_folder) # path to groundtruth

            date = date_folder[:10]
            intrinsic = INTRINSICS[date] # get intrincsic of that date

            for img_folder in ['image_02', 'image_03']:
                sub_path_to_img_folder = os.path.join(sub_path_to_date_folder, img_folder) # subpath to image_02 or image_03
                gt_path = os.path.join(KITTI_GT_PATH, sub_path_to_img_folder)

                img_fn_list = sorted(os.listdir(gt_path)) # list of png file
                for img_fn in img_fn_list:
                    normal_folder = os.path.join(KITTI_NORMALS_PATH, sub_path_to_img_folder) # stored directory
                    if not os.path.exists(normal_folder):
                        os.makedirs(normal_folder)

                    gt_img_path = os.path.join(KITTI_GT_PATH, sub_path_to_img_folder, img_fn) # whole path to png files
                    normal_img_path = os.path.join(normal_folder, img_fn)
 
                    if not os.path.exists(normal_img_path):
                        processing_args.append((gt_img_path, normal_img_path, intrinsic, 15, 0.1))
    with open('path.txt',"w") as text_file:
        for listitem in processing_args:
            text_file.write("%s\n" %listitem[0])
            text_file.write("%s\n" %listitem[1])
            

    text_file.close()
    '''
    # print("Using", num_cores, "cores")
    # pool = Pool(num_cores)
    # for _ in tqdm(pool.imap_unordered(_process, processing_args), total=len(processing_args)):
    #     pass
