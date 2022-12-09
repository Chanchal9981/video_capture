import os
import cv2
from tqdm import tqdm
import random


########### to show an image using opencv 

# img = cv2.imread("frafgfgme_3588_179.jpg")
# print(img)
# cv2.imshow("img",img)
# cv2.waitKey(1)

# # if cv2.waitKey(1) & 0xFF == ord('q'):
# #     break
    


################# video to frame operation

# vid_path = "/home/frinks1/Downloads/DP/Heidelberg/label_tag/test/new/"
# vid_path = '/media/frinks1/AU Data/Heidelberg_train_data/label_bag_tag/1000_training/'

# vid_path = '/home/frinks1/Downloads/DP/Heidelberg/label_tag/test/jsw/'
vid_path = '/home/frinks1/Downloads/DP/ACC_NEW/less_duration/'



# img_save = "/home/frinks1/Downloads/DP/Heidelberg/label_tag/test/frames/"

img_save = '/home/frinks1/Downloads/DP/ACC_NEW/extraction/'

# vid_path = "/home/frinks1/Downloads/DP/Heidelberg/bag_counting/video/3/"
# img_save = "/home/frinks1/Downloads/DP/Heidelberg/bag_counting/frames/"

random_name = ['23','r34','4e','sa','sf5','sdf2','awd','hfg','c5g','sfg','sef4','kj','vp','chmbt','rey','lil','fghgh','neo','34f']





def create_frame(vid_path,img_save,iv=3):

    # os.makedirs(img_save,exist_ok=True)
    vid_name = vid_path.split("/")[-1].split(".")[0]
    # frame_name = vid_name.split("00000000")[0]+vid_name.split("00000000")[1]

    frame_name = vid_name
    

    # os.makedirs(img_save+ vid_name +"/", exist_ok=True) ## creating folders for each and every videos separately

    print(f"---------- working with {vid_name} video---------")

    vid = cv2.VideoCapture(vid_path)

    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fps = int(vid.get(cv2.CAP_PROP_FPS))

    print("----- video information ------")
    print(f"--width: {width} \nheight: {height}" ) #\nfps: {fps}")

    fm =1
    # iv = 10




    while(True):

        ret, frame = vid.read()

        if ret:
            print(f"---working with frame: {fm} and interval: {iv}")
            rname = random.choice(random_name) ### to introduce randomization
            
            
            # if (fm>=iv) and (fm%iv ==0) and (fm > 4800): ## saving frames after interval of 20 frames

            if (fm>=iv) and (fm%iv ==0): ## saving frames after interval of 20 frames

                # cv2.imwrite(img_save+ vid_name + f"/interval_{iv}/"+f"{rname}_{frame_name}_{fm}.jpg",frame)
                cv2.imwrite(img_save+ vid_name + f"/interval_{iv}/"+f"{rname}_{frame_name}_{fm}.jpg",frame)

            # else:
                # break

            fm+=1 ### increasing the frame count
            # cv2.imshow("frame", frame)



            



            if cv2.waitKey(1) & 0xFF == ord('q'):
                vid.release()
                break

        else:
            print("--- The video is either completed or not readable. Please try with a different video. ---")
            break




    # vid.release()
    # cv2.destroyAllWindows()



def main(vid_path):

    vids = [vid_path+v for v in sorted(os.listdir(vid_path))] ### for all videos 
    # vids = [vid_path+v for v in sorted(os.listdir(vid_path))][10:] ### for all videos 



    ### if you eant to work with some selected videos

    # selected_videos = ["ch01_00000000363000000.mp4","ch01_00000000364000000.mp4","ch01_00000000365000000.mp4","ch01_00000000366000000.mp4","ch01_00000000367000000.mp4",
    #                     "ch01_00000000368000000.mp4","ch01_00000000370000000.mp4","ch01_00000000372000000.mp4"]

    # vids = [vid_path+v for v in sorted(os.listdir(vid_path)) if v in selected_videos] 


    # if len(selected_videos)  == len(vids):
        # print(f" LEN of both lists matched!!! working with: {vids} videos.")

    print(f"----- PROCESS STARTED -----")
    
    # fps_list = [5,7,9,10,12,15]

    for v in tqdm(vids):
        fps_list = [3] ##5
        vid_name = v.split("/")[-1].split(".")[0]


        for iv in fps_list:
            os.makedirs(img_save+ vid_name + f"/interval_{iv}/", exist_ok=True)
        
            create_frame(v,img_save,iv)

    
    print(f"----- TASK COMPLETED -----")



#### calling the function
main(vid_path)







