import numpy as np
import cv2
import os
import albumentations as A # Initialising the albumentations

aug = A.Compose([             
    A.RandomRotate90(p=0.5),
    A.RandomBrightnessContrast(brightness_limit=[0,0.2],contrast_limit=0.2,p=0.3),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.Transpose(p=0.5)
    ]) 

img_dir = "/home/frinks1/rishabh_backup/final_coffee_data/new_images"
mask_dir = "/home/frinks1/rishabh_backup/final_coffee_data/changed_masks_result" 
img_names = os.listdir(img_dir) 
max_imgs =800 
count = 0
while True:
    for img_name in img_names:
        if count < max_imgs:
            img_path = os.path.join(img_dir, img_name)
            mask_path = os.path.join(mask_dir, img_name.split(".")[0]+".tiff")
            img = cv2.imread(img_path)
            mask = cv2.imread(mask_path)             
            augmented = aug(image=img, mask=mask)
            transformed_image = augmented['image']
            transformed_mask = augmented['mask']             
            save_img_name = img_name.split(".")[0]+f"aug_{count}."+"bmp"
            save_mask_name = img_name.split(".")[0]+f"aug_{count}."+"tiff"
            # print(save_name)
            mask_save_path = os.path.join(mask_dir, save_mask_name)
            img_save_path = os.path.join(img_dir, save_img_name)             
            cv2.imwrite(mask_save_path, transformed_mask)
            cv2.imwrite(img_save_path, transformed_image)
            print(img_name, save_mask_name)
            count+=1
        else:
            print("Augumentation limit reached")
            break
    # break
