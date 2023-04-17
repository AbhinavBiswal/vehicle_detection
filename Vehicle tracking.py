import cv2
import numpy as np
import objectdetection
import math

#initialize object detection
od = objectdetection

cap = cv2.VideoCapture(0)

count = 0
center_points_prev_frame = []

tracking_objects = {}
track_id = 0

while True:
    ret, frame = cap.read()
    count += 1
    if not ret:
        break
    
    center_pts_cur_frame = []
    
    #detect objects on frame
    (class_ids , scores, boxes) = od.detect(frame)
    
    for box in boxes:
        (x, y , w, h) = box
        cx = int((x+x+w)/2)
        cy = int((y+y+h)/2)
        
        
    
    center_point.append((cx,cy))
   
    print("FRAME N",count ,x,y,w,h)
        
        
    #cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
    cv2.rectangle(frame,(x,y) , (x+w,y+h),(0,255,0),2)


if count <= 1:
     
    for pt in center_pts_cur_frame:
        for pt2 in center_points_prev_frame:
            distance = math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])
        
            if distance < 10:
                tracking_objects[track_id] = pt
                track_id += 1
else:
    tracking_objects_copy = tracking_objects.copy()
    
    for pt2 in tracking_objects_copy.items():
            center_pts_cur_frame_copy = center_pts_cur_frame.copy()
         
            object_exists = False
            for pt in center_pts_cur_frame:
                distance = math.hypot(pt2[0]-pt[0],pt2[1]-pt[1])
             
                if distance < 20:
                   tracking_objects[object_id]= pt
                   object_exists = True
                   if pt in center_pts_cur_frame_copy:
                     center_pts_cur_frame.remove(pt)
                     continue
             
             
             
             
                if not object_exists:
                    tracking_objects.pop(object_id)
             
    
                
            for pt in center_pts_cur_frame :
              tracking_objects[object_id] = pt
              track_id += 1
                 
        
            for object_id , pt in tracking_objects.items():
              cv2.circle(frame, (cx,cy),5,0,(0,0,255),-1)
              cv2.putText(frame,str(object_id),(pt[0],pt[1]-7),0,1,(0,0,255),-2)
            
            print("tracking objects")    
            print(tracking_objects)    
            
            
        
        
            print("cur frame")
            print(center_pts_cur_frame)
        
        # for pt in center_pts_cur_frame:
        # cv2.circle(frame,pt,5,(0,0,255),-1)
    print("prev frame")
    print(center_points_prev_frame)
        


    cv2.imshow("Frame",frame)
    
    #make a copy of the event
center_points_prev_frame = center_pts_cur_frame.copy()
        
        
key = cv2.waitKey(0)
if key == 27:
    
    break
       
        
    
    
cap.release()
cv2.destroyAllWindows()
    


