import cv2              #to access the camera
import os
from camera import resize as rs;

def pic(file_name):
    cap=cv2.VideoCapture(0)

    folder_name=r"C:\Users\jaiva\Pictures\project_pics";
    path_name=os.path.join(folder_name,file_name);

    while True:
        isTrue, frame = cap.read()
        rframe = rs.resize(frame,2.0);
        rf= cv2.flip(frame,1)
        cv2.imshow("Take a pic",rf)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(path_name,rf)
            break;
    

    cap.release()
    cv2.destroyAllWindows()
