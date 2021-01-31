import numpy as np

def nms(box, thresh=0.5):
    x1 = box[: , 0]
    y1 = box[: , 1]
    x2 = box[: , 2]
    y2 = box[: , 3]
    score = box[: , 4]
    area = (x2 - x1+1) * (y2 - y1+1)
    order = score.argsort()[::-1]
    res = []
    while order.size > 0:
        res.append(order[0])
        xx1 = np.maximum(x1[order[0]], x1[order[1:]])
        yy1 = np.maximum(y1[order[0]], y1[order[1:]])
        xx2 = np.minimum(x2[order[0]], x2[order[1:]])
        yy2 = np.minimum(y2[order[0]], y2[order[1:]])

        w = np.maximum(xx2-xx1+1, 0.0)
        h = np.maximum(yy2-yy1+1, 0.0)
        
        intersection = w * h
        print(intersection/(area[order[0]]+area[order[1:]]-intersection))
        idx = np.where(intersection/(area[order[0]]+area[order[1:]]-intersection)<thresh)[0]
        order = order[idx+1]
    return res

if __name__ == '__main__':
    dets = np.array([[310, 30, 420, 5, 0.6],
                     [20, 20, 240, 210, 1],
                     [70, 50, 260, 220, 0.8],
                     [400, 280, 560, 360, 0.7]])
    # 设置阈值
    thresh = 0.4
    keep_dets = nms(dets, thresh)
    # 打印留下的框的索引
    # print(keep_dets)
    # print(dets[keep_dets])
        
        
    
    
