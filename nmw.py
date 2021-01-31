def iou(bbox1, bbox2):
    # bbox = [x1,y1,x2,y2,score]
    xmin = max(bbox1[0], bbox2[0])
    ymin = max(bbox1[1], bbox2[1])
    xmax = min(bbox1[2], bbox2[2])
    ymax = min(bbox1[3], bbox2[3])
    w = max(xmax - xmin, 0)
    h = max(ymax - ymin, 0)
    area1 = (bbox1[2] - bbox1[0]) * (bbox1[3] - bbox1[1])
    area2 = (bbox2[2] - bbox2[0]) * (bbox2[3] - bbox2[1])
    intersection = w * h
    return intersection/(area1+area2-intersection)
def nmw(bboxes, thresh=0.5):
    new_boxes = []
    scores = []
    for box in bboxes:
        scores.append(box[4])
    while bboxes:
        idx = scores.index(max(scores))
        bbox = bboxes.pop(idx)
        score = scores.pop(idx)
        new_box = [bbox[0]*score,bbox[1]*score,bbox[2]*score,bbox[3]*score]
        weightsum = score
        tmp = []
        for i,(box, score1) in enumerate(zip(bboxes,scores)):
            if iou(box,bbox) > thresh:
                w = score1 * iou(box, bbox)
                weightsum += w
                new_box = [new_box[0]+box[0]*w,
                           new_box[1]+box[1]*w,
                           new_box[2]+box[2]*w,
                           new_box[3]+box[3]*w]
                tmp.append(i)

        for j in tmp[::-1]:
            bboxes.pop(j)
            scores.pop(j)
        new_boxes.append([i/weightsum for i in new_box])
    return new_boxes
if __name__ == "__main__":
    # print(nmw([(10, 20, 20, 30,0.8), (20, 20, 30, 30, 0.7), (15, 25, 25, 35, 0.9)], 0.1))
    

                
                
            
    
