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

        #else:
        #    new_table_coords.append(table)
    #    y_0.append(table[1])
    #    y_1.append(table[3])
    #    area = ((table[2] - table[0]) * (table[3] - table[1]))
    #    areas.append(area)
    #max_area_table_index = max(xrange(len(areas)), key=areas.__getitem__)
    #min_y_0_table_index = min(xrange(len(y_0)), key=y_0.__getitem__)
    #max_y_1_table_index = max(xrange(len(y_1)), key=y_1.__getitem__)
    #final_table = table_coords[max_area_table_index]
    #final_table[1] = table_coords[min_y_0_table_index][1] 
    #final_table[3] = table_coords[max_y_1_table_index][3]
    #return final_table
    
    if(flag == False):
        for i in range(len(table_coords)):
            tab = table_coords[i]
            tab[0] -= 50
            tab[2] += 50
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
# Calculate Accuracy 
def cal_accuracy(coords, g_x, g_x_1, g_y, g_y_1, arr, no_of_table, file_path,write_path,filename):
    file1 = open(write_path + "\\" + filename + "_words_g.csv", "wb")
    file2 = open(write_path + "\\" + filename + "_words_d.csv", "wb")
    if((no_of_table >= 1 and len(coords) == 0) or (no_of_table == 0 and len(coords) >= 1)):
        print(" accuracy : ", 0)
        file = open(file_path, 'wb')
        file.write(str(0))
        file.close()
        return
    if(no_of_table ==  0 and len(coords) == 0):
        print(" accuracy : ", 100)
        file = open(file_path, 'wb')
        file.write(str(100))
        file.close()
        return
    g_c = []
    t_c = []
    c = 0
    for i in range(no_of_table):
        for j in range(len(arr)):
            if(arr[j].x >= g_x[i] and arr[j].y >= g_y[i] and arr[j].x <= g_x_1[i] and arr[j].y <= g_y_1[i]):
                file1.write(str(arr[j].word )+ "\r\n")
                c += 1
        g_c.append(c)
        c = 0
    c = 0
    for i in range(len(coords)):
        t_coords = coords[i]
        for j in range(len(arr)):
            if(arr[j].x >= t_coords[0] and arr[j].y >= t_coords[1] and arr[j].x <= t_coords[2] and arr[j].y <= t_coords[3]):
                file2.write(str(arr[j].word )+ "\r\n")
                c += 1
        t_c.append(c)
        c = 0
    accuracy = []
    
    if(no_of_table > 1 and len(coords) > 1):
        if(no_of_table <= len(coords)):
            table_difference = []
            for i in range(no_of_table):
                for j in range(len(coords)):
                    table_difference.append(abs(g_y[i] - coords[j][1]))
                close_table_index = min(xrange(len(table_difference)), key=table_difference.__getitem__)
                table_difference = []
                if(g_c[i] >= t_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(g_c[i] - t_c[close_table_index])) / g_c[i]) * 100))
                    accuracy.append(accr)
                elif(g_c[i] <= t_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(t_c[close_table_index] - g_c[i] )) / t_c[close_table_index]) * 100))
                    accuracy.append(accr)
        if(no_of_table > len(coords)):
            table_difference = []
            for i in range(len(coords)):
                for j in range(no_of_table):
                    table_difference.append(abs(g_y[j] - coords[i][1]))
                close_table_index = min(xrange(len(table_difference)), key=table_difference.__getitem__)
                table_difference = []
                if(t_c[i] >= g_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(t_c[i] - g_c[close_table_index])) / t_c[i]) * 100))
                    accuracy.append(accr)
                elif(t_c[i] <= g_c[close_table_index]):
                    accr = abs(100 - (float(float(abs(g_c[close_table_index] - t_c[i] )) / g_c[close_table_index]) * 100))
                    accuracy.append(accr)

    else:
        if(g_c[0] >= t_c[0]):
            accr = abs(100 - (float(float(abs(g_c[0] - t_c[0])) / g_c[0]) * 100))
            accuracy.append(accr)
        elif(g_c[0] <= t_c[0]):
            accr = abs(100 - (float(float(abs(t_c[0] - g_c[0] )) / t_c[0]) * 100))
            accuracy.append(accr)
    sum = 0
    for i in range(len(accuracy)):
        sum += accuracy[i]
    mean_accuracy = sum / len(accuracy)
    if(no_of_table > len(coords)):
        if(len(coords) == 1):
                counter = 0
                dist = 0
                dist_x = 0
                for i in range(no_of_table):
                    if(no_of_table > 1 and i < (no_of_table - 1)):
                        dist = abs(g_y_1[i] - g_y[i+1])
                        dist_x = abs(g_x[i+1] - g_x_1[i])
                    if(dist <= 250 or dist_x <= 250):
                        counter += g_c[i]
                if(counter > t_c[0]):
                    mean_accuracy = abs(100 - (float(float(abs(counter - t_c[0])) / counter) * 100))
                else:
                    mean_accuracy = abs(100 - (float(float(abs(counter - t_c[0])) / t_c[0]) * 100))
        else:
            mean_accuracy = abs(mean_accuracy - ((no_of_table - len(coords)) * float(100 / no_of_table)))
    elif(no_of_table < len(coords)):
        mean_accuracy = abs(mean_accuracy - ((len(coords) - no_of_table)) * float(100 / len(coords)))
    print(" accuracy : ", mean_accuracy)
    file = open(file_path, 'wb')
    file.write(str(mean_accuracy))
    file.close()
    file2.close()
    file1.close()
    ############## End of Function ###############################################################






