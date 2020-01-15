import numpy as np

def convolution2d_ref (image, kernel, bias):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel) + bias
        return new_image

def cov(input, filter):
    sum =input * filter
    return sum.sum()
    
def convolution2d(x, kernel, stride=1):
    """
    Convolution 2D : Do Convolution on 'x' with filter = 'kernel', stride = 'stride'
    입력 x에 대해 'kernel'을 filter로 사용하여 2D Convolution을 수행하시오.
    [Input]
    x: 2D array
    - Shape : (Height, Width)
    kernel : 2D convolution filter
    - Shape : (Kernel size, Kernel size)
    stride : Stride size (default = 1)
    - dtype : int
    [Output]
    conv_out : convolution result
    - Shape : (Conv_Height, Conv_Width)
    - Conv_Height & Conv_Width can be calculated using 'Height', 'Width', 'Kernel size', 'Stride'

    - ( int( (height – kernel_size) / stride ) + 1 , int( (width – kernel_size)/stride) + 1 )
    """
    image = x
    height, width = x.shape
    kernel_size = kernel.shape[0]
    
    # =============================== EDIT HERE ===============================
    m, n = kernel.shape
    print("kernal {}  {}".format(m,n))
    print("image  {}  {}".format(height, width))
    heightY = int((height-m)/stride ) + 1
    widthX = int( (width- m)/stride) + 1
    print("output size   {}  {}".format(heightY,widthX ))

    print(list(range(heightY)))
    print(list(range(0,m,stride)))
    conv_out =np.zeros((heightY,widthX))
    for i in range(heightY):
        for j in range(widthX):
            conv_out[i][j] = np.sum(image[i*stride:i*stride+m, j*stride:j*stride+m]*kernel)
            print(i,j,i+m,j+m)

    # =========================================================================
    return conv_out


if __name__ == '__main__':
    x = np.array([[1,0,0,0], [1,1,1,1], [0,1,0,0], [1,1,0,1]])
    kernel = np.array([[1,0,0], [0,1,1], [1,1,1]])

    x_ = np.array([[1,1,0,1,1], [0,1,0,0,1], [1,1,0,1,0], [0,0,1,1,1], [1,1,1,1,1]])
    kernel_ = np.array([[1,0,1], [1,1,1], [0,1,0]])
    print("start")
    y = convolution2d(x_,kernel_,stride=2)
    print(y)
