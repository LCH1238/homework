# 文档链接如下
# 链接：https://pan.baidu.com/s/1s5d384a3IkaMI8A7APA2mw 
# 提取码：77zx

import numpy as np
import cv2

def meanI(F, num):
    F_ = np.zeros((F.shape[0] - num + 1, F.shape[1] - num + 1))
    M = 1.0/num/num * np.ones((num, num))
    for i in range(F.shape[0]-num+1):
        for j in range(F.shape[1]-num+1):
            F_[i, j] = (F[i:i+3, j:j+3] * M).sum()
    return np.round(F_).astype(np.uint8)

def keepEdgeMean(F, num):
    F_ = np.zeros(F.shape)
    M = 1.0/num/num * np.ones((num, num))
    for i in range(F.shape[0]):
        for j in range(F.shape[1]):
            if i==0 or i == F.shape[0]-1 or j==0 or j==F.shape[1]-1:
                F_[i,j] = F[i,j]
            else :  
                F_[i, j] = (F[i-1:i+2, j-1 : j+2] * M).sum()
    return np.round(F_).astype(np.uint8)

def keepEdgeMedian(F, num):
    F_ = np.zeros(F.shape)
    for i in range(F.shape[0]):
        for j in range(F.shape[1]):
            if i==0 or i == F.shape[0]-1 or j==0 or j==F.shape[1]-1:
                F_[i,j] = F[i,j]
            else :  
                F_[i, j] = np.median(F[i-1:i+2, j-1 : j+2])
    return np.round(F_).astype(np.uint8)

if __name__ == "__main__":
    F = np.array([[2,4,6,2,1,9],[6,8,6,7,7,2],[1,3,6,6,8,8],[3,4,5,6,6,6],[1,4,6,6,2,3],[1,3,6,4,6,6]])
    print(meanI(F, 3))
    f = np.array([[1,5,255,180,200,200],[1,7,254,190,170,9],[3,7,254,190,2,6],[1,0,8,7,2,1],[1,1,6,50,2,2],[2,3,9,7,2,0]]).astype(np.uint16)
    print(keepEdgeMean(f,3))
    print(keepEdgeMedian(f,3))


