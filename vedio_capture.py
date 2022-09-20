#get a frame per second
import cv2
path=r"C:\\Users\\patid\\Downloads\\ch01_00000000000000000.mp4"
os.mkdir("vedio_to_image7")
cap = cv2.VideoCapture(path)
img_count=1
# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS) 
# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# Calculate the duration of the video in seconds
duration = frame_count / fps
second = 0
#cap.set(cv2.CAP_PROP_POS_MSEC, second * 1000) # optional
success, image = cap.read()
while success and second <= duration:
    second += 1
    cap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)
    success, image = cap.read()
    if not success:
        print("unable to read frame")
        break
    isimage_write=cv2.imwrite(f"vedio_to_image7\image{img_count}.jpg",image)
    if isimage_write:
        print(f"save img at vedio_to_image7\image{img_count}.jpg")
    cv2.imshow("vedio",image)
    if cv2.waitKey(25) & 0xff == ord('q'):
        break
    img_count+=1
cap.release()
cv2.destroyAllWindows()




# # Extract frames from video into specific folder

import cv2
import glob
from glob import glob
import os
import shutil
import random
def extractFrames(m,n):
    if not os.path.exists:
        os.makedirs(n)
    vid_files=glob(m)
    print(vid_files)
    random_name = ['23','r34','4e','sa','sf5','sdf2','awd','hfg','c5g','sfg','sef4','kj','vp','chmbt','rey','lil','fghgh','neo','34f']

    for v_f in range(len(vid_files)):
        v1=os.path.basename(vid_files[v_f])
        print(v1)
        vid_name = os.path.splitext(v1)[0]
        print(vid_name)
        output = n +'\\video_' + vid_name
        os.makedirs(output)
        print(output)


        vidcap = cv2.VideoCapture(vid_files[v_f])
        print(vidcap)
        success,image = vidcap.read()
        seconds = 2
        fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
        multiplier = fps * seconds
        count=0

        while success:
            img_name = vid_name + random.choice(random_name) + str(count) + ".jpg"
            image_path = output + "/" + img_name
            frameId = int(round(vidcap.get(1)))
            success,image = vidcap.read()
            if frameId % multiplier == 0:
                cv2.imwrite(filename = image_path, img = image)
                count+=1

        vidcap.release()
        cv2.destroyAllWindows()

        print('finished processing video {0} with frames {1}'.format(vid_files[v_f], count))
    return output # indent this less

x=("C:\\Users\\patid\\Downloads\\*.mp4")
y=("C:\\Users\\patid\\Downloads\\new_data")

z=extractFrames(x,y)


# In[ ]:




