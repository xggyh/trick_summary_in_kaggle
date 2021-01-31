import math
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
def soft_nms(bboxes, iou_thresh, thresh, mode="linear"):
    res = []
    scores = []
    for box in bboxes:
        scores.append(box[4])
    nbboxes, nscore =[],[]
    while bboxes:
        idx = scores.index(max(scores))
        bbox = bboxes.pop(idx)
        score = scores.pop(idx)
        for i,(box,score1) in enumerate(zip(bboxes,scores)):
            if iou(box, bbox) > iou_thresh:
                if mode == "linear":
                    scores[i] = score1*(1-iou(box, bbox))
                else:
                    scores[i] = scores[i] * math.exp(-iou(box, bbox)**2/10)
        
        nbboxes.append(bbox)
        nscore.append(score)
    for box,score in zip(nbboxes,nscore):
        if score>thresh:
            # print(score)
            res.append(box)
    return res

if __name__ == "__main__":
    print(soft_nms([(10, 20, 20, 30, 0.8), (20, 20, 30, 30, 0.7), (15, 25, 25, 35, 0.9)], 0.1,0.65))
    
    
