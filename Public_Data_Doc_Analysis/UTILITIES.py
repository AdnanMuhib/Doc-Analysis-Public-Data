from PIL import Image, ImageDraw
##############################################################################################
################# Drawing Confusion Matrix ###############
def confusion_matrix(X, X_1, Y, Y_1, coords, img, path, name_of_file, no_of_table, arr):
    image = Image.open(img).convert('RGBA')
    drawImg = ImageDraw.Draw(image)
    for j in range(len(arr)):
        if(no_of_table == 1):
            if(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3]):
                if(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] and arr[j].y <= Y_1[0]):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                         arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                          fill=None, outline=(0,255,0))
        if(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3]):
                if(not(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] and arr[j].y <= Y_1[0])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                         arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                          fill=None, outline=(255,223,0))
        if(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] and arr[j].y <= Y_1[0]):
                if(not(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                         arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                          fill=None, outline=(0,0,255))	
        if(not(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] and arr[j].y <= Y_1[0])):
                if(not(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                        arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                        fill=None, outline=(255,0,0))

        if(no_of_table == 2):
            if(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3]):
                if(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
                   and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
                   and arr[j].y <= Y_1[1] ):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                        arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                        fill=None, outline=(0,255,0))
            if(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3]):
                if(not(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
                   and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
                   and arr[j].y <= Y_1[1])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                         arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                          fill=None, outline=(255,223,0))
            if(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
               and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
               and arr[j].y <= Y_1[1]):
                if(not(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                         arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                          fill=None, outline=(0,0,255))	
            if(not(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
               and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
               and arr[j].y <= Y_1[1])):
                if(not(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                        arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                        fill=None, outline=(255,0,0))	

        if(no_of_table == 3):
            if(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3]):
                if(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
                   and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
                   and arr[j].y <= Y_1[1] or arr[j].x >= X[2] and arr[j].y >= Y[2] and arr[j].x <= X_1[2] and arr[j].y <= Y_1[2] ):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                        arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                        fill=None, outline=(0,255,0))
            if(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3]):
                if(not(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
                   and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
                   and arr[j].y <= Y_1[1] or arr[j].x >= X[2] and arr[j].y >= Y[2] and arr[j].x <= X_1[2] and arr[j].y <= Y_1[2])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                         arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                          fill=None, outline=(255,223,0))
            if(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
               and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
               and arr[j].y <= Y_1[1] or arr[j].x >= X[2] and arr[j].y >= Y[2] and arr[j].x <= X_1[2] and arr[j].y <= Y_1[2]):
                if(not(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                         arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                          fill=None, outline=(0,0,255))	
            if(not(arr[j].x >= X[0] and arr[j].y >= Y[0] and arr[j].x <= X_1[0] 
               and arr[j].y <= Y_1[0] or arr[j].x >= X[1] and arr[j].y >= Y[1] and arr[j].x <= X_1[1] 
               and arr[j].y <= Y_1[1] or arr[j].x >= X[2] and arr[j].y >= Y[2] and arr[j].x <= X_1[2] and arr[j].y <= Y_1[2])):
                if(not(arr[j].x >= coords[0] and arr[j].y >= coords[1] and arr[j].x <= coords[2] and arr[j].y <= coords[3])):
                    for k in range(4):
                        drawImg.rectangle([arr[j].x + k ,arr[j].y + k,
                        arr[j].x + arr[j].width + k, arr[j].y + arr[j].height + k],
                        fill=None, outline=(255,0,0))	

    image.save(path + "\\" + name_of_file + "_cm.png")
######### calculate accuracy of the detection #############
'''
def calc_accuracy(X, X_1, Y, Y_1, table_coord, img, path, name_of_file, no_of_table):
    Img  = Image.open(img)
    gray_img = Img.convert('L')
    bw = gray_img.point(lambda x: 0 if x < 128 else 255, '1')
    fo = open( path + "\\csv\\" + name_of_file + "_table_coords.csv", "a")
    g_x = X[0]
    g_y = Y[0]
    g_x_1 = X_1[0]
    g_y_1 = Y_1[0]
    d_coords = table_coord
    accuracy = 0
    print("ground truth", g_x,g_y,g_x_1,g_y_1)
    print("detected",d_coords[0],d_coords[1],d_coords[2],d_coords[3])
    Area = abs(( g_x_1 - g_x ) * ( g_y_1 - g_y))
    Area2 = abs(( d_coords[2] - d_coords[0] ) * ( d_coords[3] - d_coords[1] ))
    print("Area 1 : ",Area, "Area 2 : ", Area2)
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    total_black_pixels = 0
    width = 0
    height = 0
    check = 0
    if(no_of_table > 1):
        table_difference = []
        for i in range(no_of_table):
            table_difference.append(abs(Y[i] - table_coord[1]))
        close_table_index = min(xrange(len(table_difference)), key=table_difference.__getitem__)
        g_x = X[close_table_index]
        g_y = Y[close_table_index]
        g_x_1 = X_1[close_table_index]
        g_y_1 = Y_1[close_table_index]
        Area = abs(( g_x_1 - g_x ) * ( g_y_1 - g_y))
    if(g_x < d_coords[0] and g_y < d_coords[1] and g_x_1 > d_coords[2] and g_y_1 > d_coords[3]):
        width = abs(g_x_1 - g_x)
        height = abs(g_y_1 - g_y)
        for x in range(g_x, d_coords[0]):
            for y in range(g_y, g_y_1):
                if(bw.getpixel((x, y)) == 0):
                    b1 += 1

        for x in range(g_x_1, d_coords[2]):
            for y in range(g_y, g_y_1):
                if(bw.getpixel((x, y)) == 0):
                    b2 += 1

        for x in range(g_y, d_coords[1]):
            for y in range(g_x, g_x_1):
                if(bw.getpixel((y, x)) == 0):
                    b3 += 1

        for x in range(g_y_1, d_coords[3]):
            for y in range(g_x, g_x_1):
                if(bw.getpixel((y, x)) == 0):
                    b4 += 1
    else:
        b1 = 0
        b2 = 0
        b3 = 0
        b4 = 0
        width = abs(d_coords[0] - d_coords[2])
        height = abs(d_coords[1] - d_coords[3])
        for x in range(g_x, d_coords[0]):
            for y in range(d_coords[1], d_coords[3]):
                if(bw.getpixel((x, y)) == 0):
                    b1 += 1

        for x in range(g_x_1, d_coords[2]):
            for y in range(d_coords[1], d_coords[3]):
                if(bw.getpixel((x, y)) == 0):
                    b2 += 1

        for x in range(g_y, d_coords[1]):
            for y in range(d_coords[0], d_coords[2]):
                if(bw.getpixel((y, x)) == 0):
                    b3 += 1

        for x in range(g_y_1, d_coords[3]):
            for y in range(d_coords[0], d_coords[2]):
                if(bw.getpixel((y, x)) == 0):
                    b4 += 1

    total_black_pixels = b1 + b2 + b3 + b4

    if(b1 == height and b2 == height and b3 == width and b4 == width):
        check = 0
    elif(b1 == height and b2 <= 20 and b3 <= 20 and b4 <=20 ):
        check = 0
    elif(b2 == height and b1 <= 20 and b3 <= 20 and b4 <=20 ):
        check = 0
    elif(b3 == width and b2 <= 20 and b1 <= 20 and b4 <=20 ):
        check = 0
    elif(b4 == width and b2 <= 20 and b3 <= 20 and b1 <=20 ):
        check = 0
    elif(b1 <= 20 and b2 <= 20 and b3 <= 20 and b4 <=20 ):
        check = 0
    elif(total_black_pixels == 0):
        check = 0
    else:
        check = 1

    if(check == 1):
        accuracy = abs(float(100 - (float(abs(Area-Area2))/Area) * 100))
        if(no_of_table > 1):
            error = 100 / no_of_table
            accuracy = abs(accuracy - (error * (no_of_table - 1)))        
        print("Accuracy : ", accuracy)
        fo.write("\r\n" + str(accuracy) + "%" + "," + "accurate")
    else:
        fo.write("\r\n" + "100%" + "," + "accurate")

    fo.close()
    '''
############## End of Function ###############################################################

##############################################################################################
######### Function to remove extra table 
def remove_wrong_table(table_coords):
    max_area_table_index = 0
    flag = False
    areas = []
    y_0 = []
    y_1 = []
    table_distances = []
    new_table_coords = []
    check = 0
    k = 0
    for i in range(len(table_coords)):
        table = table_coords[i]   
        if(check == 0):     
            
            if((len(table_coords) > 1) and i < len(table_coords) - 1):
                # if both tables are detected on the same line then they should be desolved into one
                if(table_coords[i+1][1] == table[1]):
                    check = 1
                    flag = True
                    k = i+1+1
                    new_table = []
                    # assigning minimum x_0 position for the newly formed joint table
                    new_table.append(min(table_coords[i+1][0], table[0]))
                    # assigning y_0 position for the newly formed joint table
                    new_table.append(table[1])
                    # assigning maximum x_1 position for the newly formed joint table
                    new_table.append(max(table_coords[i+1][2], table[2]))
                    # assigning maximum y_1 position for the newly formed joint table
                    new_table.append(max(table_coords[i+1][3], table[3]))
                    
                    # adding new table coordinates to the list of new_table_coords
                    new_table_coords.append(new_table)
                else:
                    # calculating distance between two table
                    dist = abs(table_coords[i+1][1] - table[3])
                    
                    # cheking if the distance between two lies in specific range

                    if(dist <= 190):
                        check = 1
                        flag = True
                        k = i+1+1
                        new_table = []
                        # assigning minimum x_0 position for the newly formed joint table
                        new_table.append(min(table_coords[i+1][0], table[0]))
                        # assigning y_0 position for the newly formed joint table
                        new_table.append(table[1])
                        # assigning maximum x_1 position for the newly formed joint table
                        new_table.append(max(table_coords[i+1][2], table[2]))
                        # assigning maximum y_1 position for the newly formed joint table
                        new_table.append(max(table_coords[i+1][3], table[3]))
                    
                        # adding new table coordinates to the list of new_table_coords
                        new_table_coords.append(new_table)
                        #table_distances.append(dist)
                    else:
                        new_table_coords.append(table)                      
    for i in range(k,len(table_coords)):
        tables = table_coords[i]
        new_table_coords.append(tables)
    if(flag == False):
        for i in range(len(table_coords)):
            tab = table_coords[i]
            #tab[0] -= 50
            #tab[2] += 50
            table_coords[i] = tab
        return table_coords, flag
    return new_table_coords, flag

############## End of Function ###############################################################

############ Extract Table Words through Html ######################

def extract_table_words(write_path, name_of_file, coords, arr):
    ar = []
    for i in range(len(arr)):
        if(arr[i].x >= coords[0] and arr[i].y >= coords[1] and arr[i].x <= coords[2] and arr[i].y <= coords[3]):
            ar.append(arr[i].x)
    min_value = min(ar)
    left = 30
    file = open(write_path + "\\html\\" + name_of_file + "_table_words.html", "wb")
    file.write("<html>\r\n<style>\r\ntable{\r\n border:2px solid black;\r\nwidth:" + 
    str(abs(coords[2]-coords[0]) + 50) + "px;\r\nheight:" + str(abs(coords[3]-coords[1]) + 50) +
    "px;}\r\n</style>\r\n<body>\r\n<table>\r\n<tr>\r\n")
    previous_word_y = 0
    y = 0
    top = 40
    t = 0
    a = 0
    l = 0
    b = 0
    bool = 0
    for i in range(len(arr)):
        if(arr[i].x >= coords[0] and arr[i].y >= coords[1] and arr[i].x <= coords[2] and arr[i].y <= coords[3]):
            if(bool == 0):
                previous_word_y = arr[i].y
                bool = 1
            if(arr[i].y != previous_word_y):
                top = 40
                t = abs(arr[i].y - y)
                a = t + a
                top = top + a 
                file.write ('\r\n</tr>\r\n<tr>\r\n')
                previous_word_y = arr[i].y
            y = arr[i].y
            if(arr[i].x == min_value):
                left = 30
            else:
                left = 30
                l = abs(arr[i].x - min_value)
                left = left + l
            file.write ('<td style= "position:absolute; left:' + str(left) + '; top:'+ str(top) + '">' + str(arr[i].word) + "</td> \r\n")
    file.write("</tr>\r\n</table>\r\n</body>\r\n </html>")
    file.close()

################## End of Function ####################################

##############################################################################################
###### Calculate Y Cut for column detection 
def calc_y_cut (img , coord, file_path):
    drawImg  = Image.open(img)
    im2 =  drawImg
    draw = ImageDraw.Draw(drawImg)
    # drawing detected table
    #for i in range(len(coord)):
    draw.rectangle(coord, fill = None, outline = (255, 0 , 0))
    # converting to gray
    gray_img = im2.convert('L')
    # converting to Binary Image
    bw = gray_img.point(lambda x: 0 if x < 128 else 255, '1')
    for i in range(len(coord)):
        table = coord
        ycounts = 0
        spx = 0
        spy = 0
        epx = 0
        epy = 0
        y_start = table[1]
        fpx = 0
        fpy = 0
        check = 0
        white = 0
        black = 0
        ar = []
        thr = (table[2] - table[0]) / 20
        for x in range(table[0], table[2]):
            for y in range(table[1], table[3]):
                if((bw.getpixel((x, y))) == 0):
                    ycounts += 1
            if(ycounts == 0 or ycounts == 1 or ycounts == 2 or ycounts == 3 ):
                white += 1
            if(check == 0):
                if(ycounts == 0 or ycounts == 1 or ycounts == 2 or ycounts == 3):
                    spx = x
                    check = 1
            else:
                if(ycounts > thr ):
                    epx = x
                    epy = table[3]
                    fpx = (spx + epx) / 2
                    if(epx != spx):
                        if(white > 6):
                            draw.line((fpx, y_start, fpx, epy), fill =  (255, 0, 0), width = 2)
                            ar.append(fpx)
                            check = 0
                            white = 0
            ycounts = 0
    drawImg.save(file_path)
    return ar
############## End of Function ###############################################################


##############################################################################################
# Calculate Accuracy by Counting Wordsin Ground truth tables and in Detected tables
def cal_accuracy_words(coords, g_x, g_x_1, g_y, g_y_1, arr, no_of_table, file_path):
    # check no_of_table(ground truth tables) greater than 1 while detected is zero or
    #  ground truth is zero while detected greater than 1 accuracy is zero
    if((no_of_table >= 1 and len(coords) == 0) or (no_of_table == 0 and len(coords) >= 1)):
        print(" accuracy : ", 0)
        file = open(file_path, 'wb')
        file.write(str(0))
        file.close()
        return
    #  check ground truth table is zero and detected is also zero then accuracy is 100 percent
    if(no_of_table ==  0 and len(coords) == 0):
        print(" accuracy : ", 100)
        file = open(file_path, 'wb')
        file.write(str(100))
        file.close()
        return
     # array to store the number of words in ground truth tables
    g_c = []
    # array to store the number of words in detected tables
    t_c = []
     # counter for words
    c = 0
    # count number of words of ground truth tables
    for i in range(no_of_table):
        for j in range(len(arr)):
            # if word x position greater or equal ground truth table x position and less or equal ground truth x_1 position
            # and word y position greater or equal ground truth table y position and less or equal ground truth y_1 position
            # then the word exist in this table 
            if(arr[j].x >= g_x[i] and arr[j].y >= g_y[i] and arr[j].x <= g_x_1[i] and arr[j].y <= g_y_1[i]):
                c += 1
        # append each words counter in array
        g_c.append(c)
        c = 0
    c = 0
    # count number of words of detected tables
    for i in range(len(coords)):
        # get single table
        t_coords = coords[i]
        for j in range(len(arr)):
            # if word x position greater or equal detected table x position and less or equal detected x_1 position
            # and word y position greater or equal detected table y position and less or equal detected y_1 position
            # then the word exist in this table
            if(arr[j].x >= t_coords[0] and arr[j].y >= t_coords[1] and arr[j].x <= t_coords[2] and arr[j].y <= t_coords[3]):
                c += 1
        t_c.append(c)
        c = 0
    accuracy = []
    # if ground truth tables and also detected tables greater than 1
    if(no_of_table > 1 and len(coords) > 1):
         # if ground truth tables is less than detected
        if(no_of_table <= len(coords)):
            # array to store the distance from every detected table
            # to check the close table with ground truth table
            table_difference = []
            # loop for calculate the difference and append to array of table_difference
            for i in range(no_of_table):
                for j in range(len(coords)):
                    table_difference.append(abs(g_y[i] - coords[j][1]))
                # getting the index of close table by getting the index of minimum difference value
                close_table_index = min(xrange(len(table_difference)), key=table_difference.__getitem__)
                table_difference = []
                # if number of ground truth table words is greater or 
                # equal to number of detected table words then 
                # we subtract detected words from ground truth table words 
                # and divide ground truth table words 
                if(g_c[i] >= t_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(g_c[i] - t_c[close_table_index])) / g_c[i]) * 100))
                    accuracy.append(accr)
                # if number of ground truth table words is less or 
                # equal to number of detected table words then 
                # we subtract ground truth table words from detected table words 
                # and divide detected table words
                elif(g_c[i] <= t_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(t_c[close_table_index] - g_c[i] )) / t_c[close_table_index]) * 100))
                    accuracy.append(accr)
        # if number of gorund truth tables is greater then detected
        if(no_of_table > len(coords)):
            # array to store the distance from every detected table
            # to check the close table with ground truth table
            table_difference = []
            # loop to calculate the difference and append to array of table_difference
            for i in range(len(coords)):
                for j in range(no_of_table):
                    table_difference.append(abs(g_y[j] - coords[i][1]))
                # getting the index of close table by getting the index of minimum difference value
                close_table_index = min(xrange(len(table_difference)), key=table_difference.__getitem__)
                table_difference = []
                # if number of ground truth table words is less or 
                # equal to number of detected table words then 
                # we subtract ground truth table words from detected table words 
                # and divide detected table words
                if(t_c[i] >= g_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(t_c[i] - g_c[close_table_index])) / t_c[i]) * 100))
                    accuracy.append(accr)
                # if number of ground truth table words is greater or 
                # equal to number of detected table words then 
                # we subtract detected words from ground truth table words 
                # and divide ground truth table words
                elif(t_c[i] <= g_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(g_c[close_table_index] - t_c[i] )) / g_c[close_table_index]) * 100))
                    accuracy.append(accr)
    # if ground truth and detected table is equal to one
    else:
        # if number of ground truth table words is greater or 
        # equal to number of detected table words then 
        # we subtract detected words from ground truth table words 
        # and divide ground truth table words
        if(g_c[0] >= t_c[0]):
            accr = abs(100 - (float(float(abs(g_c[0] - t_c[0])) / g_c[0]) * 100))
            accuracy.append(accr)
        # if number of ground truth table words is less or 
        # equal to number of detected table words then 
        # we subtract ground truth table words from detected table words 
        # and divide detected table words
        elif(g_c[0] <= t_c[0]):
            accr = abs(100 - (float(float(abs(t_c[0] - g_c[0] )) / t_c[0]) * 100))
            accuracy.append(accr)
    sum = 0
    # add all tables accuracy
    for i in range(len(accuracy)):
        sum += accuracy[i]
    # calculate mean accuracy 
    mean_accuracy = sum / len(accuracy)
    # if ground truth tables is greater than detected
    if(no_of_table > len(coords)):
        # if detected is one 
        if(len(coords) == 1):
                counter = 0
                dist = 0
                dist_x = 0
                # loop for calculate vertical or horizontal distance between 
                # ground truth table which is lie in detected
                for i in range(no_of_table):
                    if(no_of_table > 1 and i < (no_of_table - 1)):
                        dist = abs(g_y_1[i] - g_y[i+1])
                        dist_x = abs(g_x[i+1] - g_x_1[i])
                    # if distance is less or equal to 250 
                    # pixels then its mean the detected table is one and correctly detected
                    # even of tables marked in ground truth are more than one
                    if(dist <= 250 or dist_x <= 250):
                        # count all words of these tables 
                        counter += g_c[i]
                # if counter words is greater than detected 
                # then divide counter 
                if(counter > t_c[0]):
                    mean_accuracy = abs(100 - (float(float(abs(counter - t_c[0])) / counter) * 100))
                else:
                    mean_accuracy = abs(100 - (float(float(abs(counter - t_c[0])) / t_c[0]) * 100))
        # if detected table is not equal to one 
        # but gorund truth table is greater than detected
        # its mean some tables is not detect
        #  then we subtract
        else:
            mean_accuracy = abs(mean_accuracy - ((no_of_table - len(coords)) * float(100 / no_of_table)))
    elif(no_of_table < len(coords)):
        mean_accuracy = abs(mean_accuracy - ((len(coords) - no_of_table)) * float(100 / len(coords)))
    print(" accuracy : ", mean_accuracy)
    # file open
    file = open(file_path, 'wb')
    # write accuracy in file
    file.write(str(mean_accuracy))
    file.close()
    print("\nWords Accuracy Computed.....\n")
############## End of Function ###############################################################

##############################################################################################
######calculating accuracy by checking the pixels in intesecting areas of tables 

def calc_accuracy_pixels(X, X_1, Y, Y_1, table_coord, img, path, name_of_file, no_of_table,arr):
    # open image from img path
    Img  = Image.open(img)
    # image change in gray image
    gray_img = Img.convert('L')
    # gray image change in black and white image
    bw = gray_img.point(lambda x: 0 if x < 128 else 255, '1')
    # file open where accuracy write
    file = open( path + "\\Pixels_Accuracy\\" + name_of_file + "_accuracy_pixels.csv", "wb")
    accuracy = 0
    a = 0
    mean_accuracy = 0
    total_accur = 0
    # check no_of_table(ground truth tables) greater than 1 while detected is zero or
    #  ground truth is zero while detected greater than 1 accuracy is zero
    if((no_of_table >= 1 and len(table_coord) == 0) or (no_of_table == 0 and len(table_coord) >= 1)):
        print(" accuracy : ", 0)
        file = open(path + "\\Pixels_Accuracy\\" + name_of_file + "_accuracy_pixels.csv", "wb")
        file.write(str(0))
        file.close()
        return
    #  check ground truth table is zero and detected is also zero then accuracy is 100 percent 
    if(no_of_table ==  0 and len(table_coord) == 0):
        print(" accuracy : ", 100)
        file = open(path + "\\Pixels_Accuracy\\" + name_of_file + "_accuracy_pixels.csv", "wb")
        file.write(str(100))
        file.close()
        return
    # array to store the number of words in ground truth tables
    g_c = []
    # array to store the number of words in detected tables
    t_c = []
    # counter for words 
    c = 0
    # count number of words of ground truth tables 
    for i in range(no_of_table):
        for j in range(len(arr)):
            # if word x position greater or equal ground truth table x position and less or equal ground truth x_1 position
            # and word y position greater or equal ground truth table y position and less or equal ground truth y_1 position
            # then the word exist in this table 
            if(arr[j].x >= X[i] and arr[j].y >= Y[i] and arr[j].x <= X_1[i] and arr[j].y <= Y_1[i]):
                # count words
                c += 1
        # append each words counter in array
        g_c.append(c)
        c = 0
    c = 0
    # count number of words of detected tables
    for i in range(len(table_coord)):
        # get single table 
        t_coords = table_coord[i]
        for j in range(len(arr)):
            # if word x position greater or equal detected table x position and less or equal detected x_1 position
            # and word y position greater or equal detected table y position and less or equal detected y_1 position
            # then the word exist in this table 
            if(arr[j].x >= t_coords[0] and arr[j].y >= t_coords[1] and arr[j].x <= t_coords[2] and arr[j].y <= t_coords[3]):
                # count words
                c += 1
        # append each words counter in array
        t_c.append(c)
        c = 0

    # if ground truth tables and also detected tables greater than 1
    if(no_of_table >= 1 and len(table_coord) >= 1):
        # if ground truth tables is less than detected 
        if(no_of_table <= len(table_coord)):
            # array to store the distance from every detected table
            # to check the close table with ground truth table
            table_difference = []
            # loop for calculate the difference and append to array of table_difference
            for i in range(no_of_table):
                for j in range(len(table_coord)):
                    table_difference.append(abs(Y[i] - table_coord[j][1]))
                # getting the index of close table by getting the index of minimum difference value
                close_table_index = min(xrange(len(table_difference)), key=table_difference.__getitem__)
                table_difference = []
                # if number of gorund truth words is equal to number of detected words 
                # then accuracy is 100 percent 
                if(g_c[i] == t_c[close_table_index]):
                    accuracy = 100
                    # store total accuracy
                    total_accur = accuracy + total_accur
                    # count table for mean accuracy
                    a += 1
                # if number of gorund truth words is not equal to number of detected words
                # then apply xy-cut in else
                else:
                    # calculate area of ground truth
                    Area = abs(( X[i] - X_1[i] ) * ( Y_1[i] - Y[i]))
                    # calculate area of detected which is near to ground truth
                    Area2 = abs(( table_coord[close_table_index][2] - table_coord[close_table_index][0] ) * ( table_coord[close_table_index][3] - table_coord[close_table_index][1] ))
                    print("Area 1 : ",Area, "Area 2 : ", Area2)
                    b1 = 0
                    b2 = 0
                    b3 = 0
                    b4 = 0
                    total_black_pixels = 0
                    width = 0
                    height = 0
                    check = 0
                    # if ground truth x and y position less or equal to detected x and y position 
                    # and ground truth x_1 and y_1 position greater or equal to detected x_1 and y_1 psoition
                    # its mean detected table is in ground truth table
                    if(X[i] < table_coord[close_table_index][0] and Y[i] < table_coord[close_table_index][1] and X_1[i] > table_coord[close_table_index][2] and Y_1[i] > table_coord[close_table_index][3]):
                       # get gorund truth table width
                        width = abs(X[i] - X_1[i])
                        # get gorund truth table height
                        height = abs(Y_1[i] - Y[i])
                        # count black pixels in left area of table
                        for x in range(X[i], table_coord[close_table_index][0]):
                            for y in range(Y[i], Y_1[i]):
                                if(bw.getpixel((x, y)) == 0):
                                    b1 += 1
                        # count black pixels in right area of table
                        for x in range(X_1[i], table_coord[close_table_index][2]):
                            for y in range(Y[i], Y_1[i]):
                                if(bw.getpixel((x, y)) == 0):
                                    b2 += 1
                        # count black pixels in upper area of table
                        for x in range(Y[i], table_coord[close_table_index][1]):
                            for y in range(X[i], X_1[i]):
                                if(bw.getpixel((y, x)) == 0):
                                    b3 += 1
                        # count black pixels in bottom area of table
                        for x in range(Y_1[i], table_coord[close_table_index][3]):
                            for y in range(X[i], X_1[i]):
                                if(bw.getpixel((y, x)) == 0):
                                    b4 += 1
                    else:
                        b1 = 0
                        b2 = 0
                        b3 = 0
                        b4 = 0
                         # get detected table width
                        width = abs(table_coord[close_table_index][0] - table_coord[close_table_index][2])
                        # get detected table height
                        height = abs(table_coord[close_table_index][1] - table_coord[close_table_index][3])
                         # count black pixels in left area of table
                        for x in range(table_coord[close_table_index][0], X[i]):
                            for y in range(table_coord[close_table_index][1], table_coord[close_table_index][3]):
                                if(bw.getpixel((x, y)) == 0):
                                    b1 += 1
                       # count black pixels in right area of table
                        for x in range(table_coord[close_table_index][2], X_1[i]):
                            for y in range(table_coord[close_table_index][1], table_coord[close_table_index][3]):
                                if(bw.getpixel((x, y)) == 0):
                                    b2 += 1
                        # count black pixels in upper area of table
                        for x in range(table_coord[close_table_index][1], Y[i]):
                            for y in range(table_coord[close_table_index][0], table_coord[close_table_index][2]):
                                if(bw.getpixel((y, x)) == 0):
                                    b3 += 1
                        # count black pixels in bottom area of table
                        for x in range(table_coord[close_table_index][3], Y_1[i]):
                            for y in range(table_coord[close_table_index][0], table_coord[close_table_index][2]):
                                if(bw.getpixel((y, x)) == 0):
                                    b4 += 1
                    # count total pixel
                    total_black_pixels = b1 + b2 + b3 + b4
                    
                    # if black pixels equal to height or width in all boundries then its a line so check will be zero
                    if(b1 == height and b2 == height and b3 == width and b4 == width):
                        check = 0
                    # if black pixels equal to height in left side then its a line but all sides black pixel is 20 then check will zero
                    elif(b1 == height and b2 <= 20 and b3 <= 20 and b4 <=20 ):
                        check = 0
                    # if black pixels equal to height in right side then its a line but all sides black pixel is 20 then check will zero
                    elif(b2 == height and b1 <= 20 and b3 <= 20 and b4 <=20 ):
                        check = 0
                    # if black pixels equal to width in upper side then its a line but all sides black pixel is 20 then check will zero
                    elif(b3 == width and b2 <= 20 and b1 <= 20 and b4 <=20 ):
                        check = 0
                    # if black pixels equal to width in below side then its a line but all sides black pixel is 20 then check will zero
                    elif(b4 == width and b2 <= 20 and b3 <= 20 and b1 <=20 ):
                        check = 0
                    # if all sides black pixel is 20 then check will zero
                    elif(b1 <= 20 and b2 <= 20 and b3 <= 20 and b4 <=20 ):
                        check = 0
                    # if all sides pixels is zero then check will zero
                    elif(total_black_pixels == 0):
                        check = 0
                    # other wise check will be 1
                    else:
                        check = 1
                    # if check is 1 then calculate accuracy by area
                    if(check == 1):
                        # if ground truth area is greater or equal to detected then divide ground truth 
                        if(Area >= Area2):
                            accuracy = abs(float(100 - (float(abs(Area-Area2))/Area) * 100))
                        else:
                            accuracy = abs(float(100 - (float(abs(Area-Area2))/Area2) * 100))
                        a += 1
                    # if check is zero then its mean accuracy would be 100 percent
                    else:
                        accuracy = 100
                        a += 1
                    # add all accuracy one by one 
                    total_accur = accuracy + total_accur
        # if number of gorund truth tables is greater then detected
        if(no_of_table > len(table_coord)):
            # if detected is one
            if(len(table_coord) == 1):
                counter = 0
                total_Area = 0
                dist = 0
                dist_x = 0
                # loop for calculate vertical or horizontal distance between 
                # ground truth table which is lie in detected 
                for i in range(no_of_table):
                    if(no_of_table > 1 and i < (no_of_table - 1)):
                        dist = abs(Y[i] - Y[i+1])
                        dist_x = abs(X[i+1] - X[i])
                    # if distance is less or equal to 250 
                    # pixels then its mean the detected table is one and correctly detected
                    # even of tables marked in ground truth are more than one
                    if(dist <= 250 or dist_x <= 250):
                        # count all words of these tables 
                        counter += g_c[i]
                        # add area of these tables
                        Area = abs(( X[i] - X_1[i] ) * ( Y_1[i] - Y[i]))
                        print("check area",Area)
                        # calculate total area of all tables 
                        total_Area = Area + total_Area
                    else:
                        Area = abs(( X[i] - X_1[i] ) * ( Y_1[i] - Y[i]))
                        total_Area = Area + total_Area
                # if number of detected words is equal to number of counter(ground truth tables which distance is less or equal to 250) words
                # then its mean 100 percent accuracy 
                if(t_c[0] == counter):
                    accuracy = 100
                    a += 1
                    total_accur = accuracy + total_accur
                # other wise apply xy-cut method to calculate accuracy
                else:
                    # calculate area of detected table
                    Area2 = abs(( table_coord[0][2] - table_coord[0][0] ) * ( table_coord[0][3] - table_coord[0][1] ))
                    print("Area 1 : ",Area, "Area 2 : ", Area2)
                    b1 = 0
                    b2 = 0
                    b3 = 0
                    b4 = 0
                    total_black_pixels = 0
                    width = 0
                    height = 0
                    check = 0
                    # if ground truth x and y position less or equal to detected x and y position 
                    # and ground truth x_1 and y_1 position greater or equal to detected x_1 and y_1 psoition
                    # its mean detected table is in ground truth table
                    if(X[0] < table_coord[0][0] and Y[0] < table_coord[0][1] and X_1[no_of_table-1] > table_coord[0][2] and Y_1[no_of_table-1] > table_coord[0][3]):
                        # calculate width of detected table
                        width = abs(table_coord[0][0] - table_coord[0][2])
                        # calculate height of detected table
                        height = abs(table_coord[0][1] - table_coord[0][3])
                        # count black pixels in left area of table
                        for x in range(X[0], table_coord[0][0]):
                            for y in range(Y[0], Y_1[no_of_table-1]):
                                if(bw.getpixel((x, y)) == 0):
                                    b1 += 1
                        # count black pixels in right area of table
                        for x in range(X_1[0], table_coord[0][2]):
                            for y in range(Y[0], Y_1[no_of_table-1]):
                                if(bw.getpixel((x, y)) == 0):
                                    b2 += 1
                        # count black pixels in upper area of table
                        for x in range(Y[0], table_coord[0][1]):
                            for y in range(X[0], X_1[0]):
                                if(bw.getpixel((y, x)) == 0):
                                    b3 += 1
                        # count black pixels in bottom area of table
                        for x in range(Y_1[no_of_table-1], table_coord[0][3]):
                            for y in range(X[0], X_1[0]):
                                if(bw.getpixel((y, x)) == 0):
                                    b4 += 1
                    else:
                        b1 = 0
                        b2 = 0
                        b3 = 0
                        b4 = 0
                        width = abs(table_coord[0][0] - table_coord[0][2])
                        height = abs(table_coord[0][1] - table_coord[0][3])
                        for x in range(table_coord[0][0], X[0]):
                            for y in range(table_coord[0][1], table_coord[0][3]):
                                if(bw.getpixel((x, y)) == 0):
                                    b1 += 1

                        for x in range(table_coord[0][2], X_1[no_of_table-1]):
                            for y in range(table_coord[0][1], table_coord[0][3]):
                                if(bw.getpixel((x, y)) == 0):
                                    b2 += 1

                        for x in range(table_coord[0][1], Y[0]):
                            for y in range(table_coord[0][0], table_coord[0][2]):
                                if(bw.getpixel((y, x)) == 0):
                                    b3 += 1

                        for x in range(table_coord[0][3], Y_1[no_of_table-1]):
                            for y in range(table_coord[0][0], table_coord[0][2]):
                                if(bw.getpixel((y, x)) == 0):
                                    b4 += 1

                    total_black_pixels = b1 + b2 + b3 + b4
                     # if black pixels equal to height or width in all
                     #  boundries then its a line so check will be zero
                    if(b1 == height and b2 == height and b3 == width and b4 == width):
                        check = 0
                    # if black pixels equal to height in left side then its a line
                    #  but all sides black pixel is 20 then check will zero
                    elif(b1 == height and b2 <= 20 and b3 <= 20 and b4 <=20 ):
                        check = 0  
                    # if black pixels equal to height in right side then its
                    #  a line but all sides black pixel is 20 then check will zero
                    elif(b2 == height and b1 <= 20 and b3 <= 20 and b4 <=20 ):
                        check = 0
                    # if black pixels equal to width in upper side then its a
                    #  line but all sides black pixel is 20 then check will zero
                    elif(b3 == width and b2 <= 20 and b1 <= 20 and b4 <=20 ):
                        check = 0
                    # if black pixels equal to width in lower side then its a line
                    #  but all sides black pixel is 20 then check will zero
                    elif(b4 == width and b2 <= 20 and b3 <= 20 and b1 <=20 ):
                        check = 0
                    # if all sides black pixel is 20 then check will zero
                    elif(b1 <= 20 and b2 <= 20 and b3 <= 20 and b4 <=20 ):
                        check = 0
                    # if all sides pixels is zero then check will zero
                    elif(total_black_pixels == 0):
                        check = 0
                    else:
                        check = 1

                    if(check == 1):
                        # if total Area of ground truth tables which is in detected
                        #  one is greater or equal to detected area than divide ground truth area
                        if(total_Area >= Area2):
                            accuracy = abs(float(100 - (float(abs(total_Area-Area2))/total_Area) * 100))
                        else:
                            accuracy = abs(float(100 - (float(abs(total_Area-Area2))/Area2) * 100))
                        a += 1
                    else:
                        accuracy = 100 
                        a += 1

                    total_accur = accuracy + total_accur
            # if detected table is greater than one 
            else:  
                # array to store the distance from every detected table
                # to check the close table with ground truth table
                table_difference = []
                 # loop to calculate the difference and append to array of table_difference
                for i in range(len(table_coord)):
                    for j in range(no_of_table):
                        table_difference.append(abs(Y[j] - table_coord[i][1]))
                     # getting the index of close table by getting the index of minimum difference value
                    close_table_index = min(xrange(len(table_difference)), key=table_difference.__getitem__)
                    table_difference = []
                    # if number of gorund truth words is equal to number of detected words 
                    # then accuracy is 100 percent
                    if(g_c[close_table_index] == t_c[i]):
                        accuracy = 100
                        # store total accuracy
                        total_accur = accuracy + total_accur
                        # count table for mean accuracy
                        a += 1
                    # if number of gorund truth words is not equal to number of detected words
                    # then apply xy-cut in else
                    else:
                         # calculate area of ground truth which is near to detected
                        Area = abs(( X[close_table_index] - X_1[close_table_index] ) * ( Y_1[close_table_index] - Y[close_table_index]))
                        # calculate area of detected 
                        Area2 = abs(( table_coord[i][2] - table_coord[i][0] ) * ( table_coord[i][3] - table_coord[i][1] ))
                        print("Area 1 : ",Area, "Area 2 : ", Area2)
                        b1 = 0
                        b2 = 0
                        b3 = 0
                        b4 = 0
                        total_black_pixels = 0
                        width = 0
                        height = 0
                        check = 0
                        # if ground truth x and y position less or equal to detected x and y position 
                        # and ground truth x_1 and y_1 position greater or equal to detected x_1 and y_1 psoition
                        # its mean detected table is in ground truth table
                        if(X[close_table_index] < table_coord[i][0] and Y[close_table_index] < table_coord[i][1] and X_1[close_table_index] > table_coord[i][2] and Y_1[close_table_index] > table_coord[i][3]):
                            # get gorund truth table width
                            width = abs(X[close_table_index] - X_1[close_table_index])
                            # get gorund truth table height
                            height = abs(Y_1[close_table_index] - Y[close_table_index])
                            # count black pixels in left area of table
                            for x in range(X[close_table_index], table_coord[i][0]):
                                for y in range(Y[close_table_index], Y_1[close_table_index]):
                                    if(bw.getpixel((x, y)) == 0):
                                        b1 += 1
                             # count black pixels in right area of table
                            for x in range(X_1[close_table_index], table_coord[i][2]):
                                for y in range(Y[close_table_index], Y_1[close_table_index]):
                                    if(bw.getpixel((x, y)) == 0):
                                        b2 += 1
                            # count black pixels in upper area of table
                            for x in range(Y[close_table_index], table_coord[i][1]):
                                for y in range(X[close_table_index], X_1[close_table_index]):
                                    if(bw.getpixel((y, x)) == 0):
                                        b3 += 1
                            # count black pixels in bottom area of table
                            for x in range(Y_1[close_table_index], table_coord[i][3]):
                                for y in range(X[close_table_index], X_1[close_table_index]):
                                    if(bw.getpixel((y, x)) == 0):
                                        b4 += 1
                        else:
                            b1 = 0
                            b2 = 0
                            b3 = 0
                            b4 = 0
                            # get detected table width
                            width = abs(table_coord[i][0] - table_coord[i][2])
                            # get detected table height
                            height = abs(table_coord[i][1] - table_coord[i][3])
                            # count black pixels in left area of table
                            for x in range(table_coord[i][0], X[close_table_index]):
                                for y in range(table_coord[i][1], table_coord[i][3]):
                                    if(bw.getpixel((x, y)) == 0):
                                        b1 += 1
                            # count black pixels in right area of table
                            for x in range(table_coord[i][2], X_1[close_table_index]):
                                for y in range(table_coord[i][1], table_coord[i][3]):
                                    if(bw.getpixel((x, y)) == 0):
                                        b2 += 1
                            # count black pixels in upper area of table
                            for x in range(table_coord[i][1], Y[close_table_index]):
                                for y in range(table_coord[i][0], table_coord[i][2]):
                                    if(bw.getpixel((y, x)) == 0):
                                        b3 += 1
                            # count black pixels in bottom area of table
                            for x in range(table_coord[i][3], Y_1[close_table_index]):
                                for y in range(table_coord[i][0], table_coord[i][2]):
                                    if(bw.getpixel((y, x)) == 0):
                                        b4 += 1
                        # count total pixel
                        total_black_pixels = b1 + b2 + b3 + b4
                        # if black pixels equal to height or width in all boundries then its a line so check will be zero
                        if(b1 == height and b2 == height and b3 == width and b4 == width):
                            check = 0
                        # if black pixels equal to height in left side then its a line but all sides black pixel is 20 then check will zero
                        elif(b1 == height and b2 <= 20 and b3 <= 20 and b4 <=20 ):
                            check = 0 
                        # if black pixels equal to height in right side then its a line but all sides black pixel is 20 then check will zero
                        elif(b2 == height and b1 <= 20 and b3 <= 20 and b4 <=20 ):
                            check = 0
                        # if black pixels equal to height in right side then its a line but all sides black pixel is 20 then check will zero
                        elif(b3 == width and b2 <= 20 and b1 <= 20 and b4 <=20 ):
                            check = 0
                        # if black pixels equal to width in below side then its a line but all sides black pixel is 20 then check will zero
                        elif(b4 == width and b2 <= 20 and b3 <= 20 and b1 <=20 ):
                            check = 0
                        # if all sides black pixel is 20 then check will zero
                        elif(b1 <= 20 and b2 <= 20 and b3 <= 20 and b4 <=20 ):
                            check = 0
                        # if all sides pixels is zero then check will zero
                        elif(total_black_pixels == 0):
                            check = 0
                        else:
                            check = 1
                        # if check is 1 then calculate accuracy by area
                        if(check == 1):
                            # if ground truth area is greater or equal to detected then divide ground truth
                            if(Area > Area2):
                                accuracy = abs(float(100 - (float(abs(Area-Area2))/Area) * 100))
                            else:
                                accuracy = abs(float(100 - (float(abs(Area-Area2))/Area2) * 100))
                            a += 1
                        # if check is zero then its mean accuracy would be 100 percent
                        else:
                            accuracy = 100 
                            a += 1

                        total_accur = accuracy + total_accur           

   # calculate mean accuracy 
    mean_accuracy = total_accur / a
    print("accuracy", mean_accuracy)
    # write accuracy in file
    file.write("\r\n" + str(mean_accuracy) + "%" + "," + "accurate")
    file.close()
    print("\nPixels Accuracy Computed.....\n")
############## End of Function ###############################################################

##############################################################################################
################ extract tables #################################
def extract_table_wordss(write_path, name_of_file, d_coords, arr):
    # array for store x values of words 
    ar = []
    # left margin for first minimum x position of word
    left = 30
    # store the value of y position for every word to
    # compare and bring the every word on the top of the page
    y = 0
    # top margin of table words
    top = 40
    # store y differnce between two words 
    t = 0
    # used for store previous difference 
    # so that we add in next y differnce
    a = 0
    # store x differnce between two words
    l = 0
    # used for margin of next table from previous table
    p = 0
    # used for margin of next table from previous table
    s = 0
    # used for store preivous table top value
    r = 0
    # used for store minimum value of x position of word
    min_value = 0
    # open file
    file = open(write_path + "\\html\\" + name_of_file + "_table_words.html", "wb")
    file.write("<html>\r\n<style>")
    # loop used for write styles of table in html file
    for x in range(len(d_coords)):
    	
    	coordss = d_coords[x]
    	file.write("\r\n#t"+ str(x) + "{\r\n border:2px solid black;\r\nwidth:" + 
        str(abs(coordss[2]-coordss[0]) + 50) + "px;\r\nheight:" + str(abs(coordss[3]-coordss[1]) + 50) +
        'px;\r\nmargin-top:20;}')    
    file.write("\r\n</style>\r\n<body>\r\n")
    # loop for handling of multiple tables
    for z in range(len(d_coords)):
        # start set top value 
        top = 40
        a = 0
        bool = 0
        ar = []
        top = top + s
        r = top
        coords = d_coords[z]
        # loop for store all x position of words of table
        for i in range(len(arr)):
            if(arr[i].x >= coords[0] and arr[i].y >= coords[1] and arr[i].x <= coords[2] and arr[i].y <= coords[3]):
                ar.append(arr[i].x)
                
        
        file.write('<table id = "t' + str(z) + '">\r\n<tr>\r\n')
        # previous y position of every table should be change 
        # so we initialize zero for every table
        previous_word_y = 0
        # store minimum value of x position of word
        min_value = min(ar)
        # loop for write words in file
        for i in range(len(arr)):
            # check which word is part of table 
            if(arr[i].x >= coords[0] and arr[i].y >= coords[1] and arr[i].x <= coords[2] and arr[i].y <= coords[3]):
                # get previous y position of first word of table
                # then bool set 1
                if(bool == 0):
                    previous_word_y = arr[i].y
                    bool = 1
                # when y position of word will not match with previous y position
                # its mean start of new row of table
                if(arr[i].y != previous_word_y):
                    # then we set top of next row to find differnce between previous row 
                    # and next row through subtract previous from next row y value
                    top = r
                    t = abs(arr[i].y - y)
                    a = t + a
                    top = top + a 
                    file.write ('\r\n</tr>\r\n<tr>\r\n')
                    # again previous position set for next row 
                    previous_word_y = arr[i].y
                y = arr[i].y
                # set margin of left side if x position of word 
                # is equal to min value its mean word is most left side 
                # set left margin 30
                if(arr[i].x == min_value):
                    left = 30
                # otherwise we subtract minimum value from x position of next word
                # so that we can set left margin of next word 
                else:
                    left = 30
                    l = abs(arr[i].x - min_value)
                    left = left + l
                # write word in file 
                file.write ('<td style= "position:absolute; left:' + str(left) + '; top:'+ str(top) + '">' + str(arr[i].word) + "</td> \r\n")
        file.write("</tr>\r\n</table>\r\n")
        # used for margin of next table from previous table
        p = abs(coords[3]-coords[1]) + 50
        s = s + p + 20
    file.write("\r\n</body>\r\n </html>")
    file.close()
################## End of Function ####################################




