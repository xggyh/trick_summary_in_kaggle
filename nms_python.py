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
def nms(bboxes, thresh=0.5):
    # bbox: [x1,y1,x2,y2,score]
    # thresh: overlap threshold 
    res = []
    score = []
    for box in bboxes:
        score.append(box[4])
    while bboxes:
        idx = score.index(max(score))
        bbox = bboxes.pop(idx)
        score.pop(idx)
        tmp = []
        for i,box in enumerate(bboxes):
            if iou(box, bbox) > thresh:
                tmp.append(i)
        for i in tmp[::-1]:
            bboxes.pop(i)
            score.pop(i)
        res.append(bbox)
    return res

if __name__ == "__main__":
    print(nms([(10, 20, 20, 30, 0.8), (20, 20, 30, 30, 0.7), (15, 25, 25, 35, 0.9)], 0.142875))
                
    
