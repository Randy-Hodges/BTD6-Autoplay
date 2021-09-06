def round_finished():
    '''Checks if the round is finished by looking at how bright the pixels of Psi's first ability is'''
    img0 = ImageGrab.grab(bbox = (int(170/test_scrn_width*int(screensize[0])), # left bound
                            int(1020/test_scrn_height*int(screensize[1])), # upper bound
                            int(210/test_scrn_width*int(screensize[0])), # right bound
                            int(1060/test_scrn_height*int(screensize[1]))  # lower bound
                        )
    )
 
    img = np.asfarray(img0)
    height = len(img) 
    width = len(img[0])
    img.setflags(write=1)
    total = 0
    n = height*width
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = img[loop1,loop2]
            total += r
    mean = total/n
    if 104 < mean < 108: 
        print(f'mean: {mean}') 
    return True if 100 < mean < 115 else False