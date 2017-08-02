"""Its testing document analysis interface getting the predictions and drawing the structure.
    (Updated 19/4/17)"""

##############################################################################################
# Adding set of the modules important for this class
import DocumentParser as DP
import DataCollector as DC
import FeatureExtraction as FE
import WekaMachineLearning as WML
import PostProcessor as PP
import StructureIdentification as Struct_I
import CellDrawing as CD 

import os
import re
import weka.core.jvm as jvm
import traceback
import sys
from PIL import Image, ImageDraw

##############################################################################################
######### calculate accuracy of the detection #############
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
    if(no_of_table == 2):
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
        width = g_x_1 - g_x
        height = g_y_1 - g_y
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
        accuracy = float(100 - (float(Area-Area2)/Area) * 100)
        if(no_of_table == 2):
            accuracy = accuracy - 50        
        print("Accuracy : ", accuracy)
        fo.write("\r\n" + str(accuracy) + "%" + "," + "accurate")
    else:
        fo.write("\r\n" + "100%" + "," + "accurate")

    fo.close()
############## End of Function ###############################################################

##############################################################################################
######### Function to remove extra table 
def remove_wrong_table(table_coords):
    max_area_table_index = 0
    areas = []
    y_0 = []
    y_1 = []
    for i in range(len(table_coords)):
        table = table_coords[i]
        y_0.append(table[1])
        y_1.append(table[3])
        area = ((table[2] - table[0]) * (table[3] - table[1]))
        areas.append(area)
    max_area_table_index = max(xrange(len(areas)), key=areas.__getitem__)
    min_y_0_table_index = min(xrange(len(y_0)), key=y_0.__getitem__)
    max_y_1_table_index = max(xrange(len(y_1)), key=y_1.__getitem__)
    final_table = table_coords[max_area_table_index]
    final_table[1] = table_coords[min_y_0_table_index][1] 
    final_table[3] = table_coords[max_y_1_table_index][3]
    return final_table
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
    for i in range(len(coord)):
        draw.rectangle(coord[i], fill = None, outline = (255, 0 , 0))
    # converting to gray
    gray_img = im2.convert('L')
    # converting to Binary Image
    bw = gray_img.point(lambda x: 0 if x < 128 else 255, '1')
    for i in range(len(coord)):
        table = coord[i]
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
# Main function for document analysis

def main(table, img, ocr, name_of_file, arff, out_img, write_path, model_file):
    # Creating instances for cross library work
    document_parser = DP.DocumentParser()
    feature_extractor = FE.FeatureExtraction()
    weka_machine_learning = WML.WekaMachineLearning()
    structure_identification = Struct_I.StructureIdentification()
    post_processor = PP.PostProcessor()
    cell_drawing = CD.CellDrawing()

    print("Write Path",write_path)
    print("Name of File",name_of_file)
    file = open(write_path + "\\csv\\" + name_of_file + "_table_coords.csv", "wb")

    # Read table xml file and calculate the line spaces
    no_of_table, X, Y, X_1, Y_1, width, height = document_parser.table_to_array(table)

    # Drawing the Ground Truth of the Table on image
    im = Image.open(img).convert('RGBA')
    draw_image = ImageDraw.Draw(im)
    if(no_of_table!=None):
        for i in range(no_of_table):
            for j in range(3):
                draw_image.rectangle([X[i]+j, Y[i]+j,  X_1[i] + j, Y_1[i] + j], fill=None, outline=(0, 255, 0))
            Area = (( X_1[i] - X[i] ) * ( Y_1[i] - Y[i] ))
            file.write ('Ground Truth' + ',' + str(X[i]) + ',' + str(Y[i]) + ',' + str(X_1[i]) 
        	+ ',' + str(Y_1[i]) + ',' + str(Area) + '\r\n')


    # Read the word list xml file
    no_of_words, total_width, total_height, words, word_X, word_Y, word_Width, word_Height\
        = document_parser.word_to_array(ocr)
    # Assigning values to struct object and creating an array.  this is array
    # is basically
    # An array of objects
    arr_of_objects = feature_extractor.assigning_values_to_the_struct(no_of_words, word_X,
                                                                      word_Y, word_Width,
                                                                      word_Height, words, 
                                                                      X, Y, X_1, Y_1)
    # Sorting an array because initially its not in order
    sorted_array_y = feature_extractor.sort_array(arr_of_objects)
    # There is a difference in different words vertically in a line.  So
    # eliminating that
    # difference to sort perfectly
    eliminated_diff = feature_extractor.eliminate_y_diff(sorted_array_y)
    # After sorting y then we need to sort every x in that specific y
    sorted_array_x = feature_extractor.sort_array_by_x(eliminated_diff)
    # Distance is then calculated between words for training purpose
    dist_calculted_arr = feature_extractor.calculate_dist(sorted_array_x)
    # Now the list of objects are stored in an array for writing it into csv
    array_of_objects = feature_extractor.objects_to_array(dist_calculted_arr)
    # Getting the predictions for the specific arff file
    prediction = weka_machine_learning.weka_cross_validation(model_file, arff)
    # Adding prediction to the array for further easy use
    p_arr = post_processor.prediction_to_array(dist_calculted_arr, prediction)
    # Output look before applying the ground truth
    #cell_drawing.draw_prediction(p_arr, img, name_of_file + "_before")
    # Applying ground truth
    n_arr = post_processor.ground_truth_x(p_arr, prediction)
    # Output look like after applying the ground truth
    #cell_drawing.draw_prediction(n_arr, img, name_of_file + "_after")
    # Detect table
    s_arr, table_coord, table_coord_actual = structure_identification.detect_tables(img, n_arr, out_img)

    #removing wrong detected tables
    final_table = remove_wrong_table(table_coord_actual)
    
    
    ## drawing detected table
    #for i in range(len(table_coord_actual)):
    #    draw_image.rectangle(table_coord_actual[i], fill = None, outline = (255, 0 , 0))
    #    coord = table_coord_actual[i]
    #    Area2 = (( coord[0] - coord[2] ) * ( coord[1] - coord[3] )) 
    #    file.write ('Detected' + ',' + str(coord[0]) + ',' + str(coord[1]) + ',' + str(coord[2]) 
    #    	+ ',' + str(coord[3]) + ',' + str(Area2) + '\r\n')
    #im.save(write_path + "\\" + name_of_file + "_accuracy.png")
    #file.close()

    # drawing detected table
    draw_image.rectangle(final_table, fill = None, outline = (255, 0 , 0))
    coord = final_table
    Area2 = (( coord[0] - coord[2] ) * ( coord[1] - coord[3] )) 
    file.write ('Detected' + ',' + str(coord[0]) + ',' + str(coord[1]) + ',' + str(coord[2]) 
        + ',' + str(coord[3]) + ',' + str(Area2) + '\r\n')
    im.save(write_path + "\\" + name_of_file + "_accuracy.png")
    file.close()

    # call to function of calculating Y cut
    ar = calc_y_cut(img, final_table, write_path + "\\" + name_of_file + "_column.png")
    
    calc_accuracy(X, X_1, Y, Y_1, final_table, img, write_path, name_of_file, no_of_table)
    
    # Extracting words of detected table region and writing them to csv
    extract_table_words(write_path,name_of_file,final_table,arr_of_objects)
    
    # Detect words in the table
    cells_arr = structure_identification.detecting_cell(img, s_arr,
                                                        write_path + "\\" 
                                                        + name_of_file + "_cells.png",
                                                        table_coord) 
    # Detect rows in the table
    structure_identification.detect_rows(img, cells_arr, write_path + "\\" 
                                                        + name_of_file  + "_rows.png")
    # Detecting the cells, rows, columns and tables
    structure_identification.detect_components(img, cells_arr, write_path + "\\" 
                                                        + name_of_file +
                                               "_struct_identification.png")
############## End of Function ###############################################################

##############################################################################################
# batch processor for running it in loop over all the lements in that directory
def batch_processor():
    dir_img = "F:\\KICS - Research Officer\\Document Analysis\\DATA SET\\Test Data\\Bulk"
    extension = ".png"
    # Get the files in the directory
    file_list = os.listdir(dir_img)
    # Calling the main function with the files
    dir_data = "F:\KICS - Research Officer\CVML\Document Analysis\DATA SET\Test Data\OCR_gt"
    dir_out = "F:\KICS - Research Officer\CVML\Document Analysis\DATA SET\Test Data\output"
    for file in file_list:
        name_of_file = re.split(extension, file)[0]
        ocr = dir_data + "\\" + name_of_file + "_ocr.xml"
        img = dir_img + "\\" + name_of_file + ".png"
        table = dir_data + "\\" + name_of_file + ".xml"
        out = dir_out + "\\" + name_of_file + "_image_out.png"
        file_to_write = dir_out + "\\" + name_of_file
        arff = dir_out + "\\" + name_of_file + ".csv_arff.arff"
        out_img = dir_out + "\\" + name_of_file + "_table.png"
        main(table, img, ocr, file_to_write, arff, out_img)
    # end of the batch processing
    return
############## End of Function ###############################################################

##############################################################################################
# For cross compilation
def setup_main(path, file_name, write_path, model_file):
    table = path + "\\" + file_name + ".xml"
    ocr = path + "\\" + file_name + "_ocr.xml"
    img = path + "\\" + file_name + ".png"
    arff = path + "\\" + file_name + ".csv_arff.arff"
    file_to_write = file_name
    out_img = write_path + "\\" + file_name + "_table.png"
    main(table, img, ocr, file_to_write, arff, out_img, write_path, model_file)
    
    return
############## End of Function ###############################################################

##############################################################################################
### batch Processor new
import ntpath
def batch_processor_current():
    bulk_folder = "F:\\KICS - Research Officer\\Document Analysis\\DATA SET\\Test Data\\Bulk"
    extension = ".png"
    model_file = "Model\\Model.model"
    write_path = ntpath.expanduser('~\\Documents\\Document Analysis')
    file_path = bulk_folder
    # Get the files in the directory
    file_list = os.listdir(bulk_folder)
    for file in file_list:
        if file.endswith(".png"):
            name_of_file = re.split(extension, file)[0]
            setup_main(file_path, name_of_file, write_path, model_file)
            
    return
############## End of Function ###############################################################


##############################################################################################
# Command line arguments
if __name__ == "__main__":
    jvm.start()
    batch_processor_current()
    jvm.stop()
##############################################################################################
########################################END###################################################
##############################################################################################



