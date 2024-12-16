def rectangles_inside(a, b, x, y):
    #Orientacion Original
    originalOrientation = (x // b) * (y // a) 
    remainderX = x % b
    extra_from_remainderX = (remainderX // a) * (y // b)
    
    #Orientacion Rotada
    rotatedOrientation = (x // a) * (y // b)
    remainderX_rotated = x % a
    extra_from_remainderX_rotated = (remainderX_rotated // b) * (y // a)
    
    total_option_1 = originalOrientation + extra_from_remainderX
    total_option_2 = rotatedOrientation + extra_from_remainderX_rotated
    
    return max(total_option_1, total_option_2)


print(rectangles_inside(2,2,1,10))
