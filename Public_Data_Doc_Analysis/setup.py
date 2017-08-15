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
import UTILITIES as UT
import os
import ntpath
import re
import weka.core.jvm as jvm
import traceback
import sys
from PIL import Image, ImageDraw

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

    # Read table xml file and calculate the line spaces
    no_of_table, X, Y, X_1, Y_1, width, height = document_parser.table_to_array(table)
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
    #cell_drawing.draw_prediction(p_arr, img, write_path + "\\" + name_of_file + "_before")
    # Applying ground truth
    n_arr = post_processor.ground_truth_x(p_arr, prediction)
    # Output look like after applying the ground truth
    #cell_drawing.draw_prediction(n_arr, img,  write_path + "\\" + name_of_file + "_after")
    # Detect table
    s_arr, table_coord, table_coord_actual = structure_identification.detect_tables(img, n_arr, out_img)

    #removing wrong detected tables
    final_table, flag = UT.remove_wrong_table(table_coord_actual)
    while(flag):
        final_table, flag = UT.remove_wrong_table(final_table)

    

    ## Drawing the Ground Truth of the Table on image
    #im = Image.open(img).convert('RGBA')
    #draw_image = ImageDraw.Draw(im)
    #if(no_of_table!=None):
    #    for i in range(no_of_table):
    #        for j in range(3):
    #            draw_image.rectangle([X[i]+j, Y[i]+j,  X_1[i] + j, Y_1[i] + j], fill=None, outline=(0, 255, 0))
    #        Area = (( X_1[i] - X[i] ) * ( Y_1[i] - Y[i] ))
         #   file.write ('Ground Truth' + ',' + str(X[i]) + ',' + str(Y[i]) + ',' + str(X_1[i]) 
        	#+ ',' + str(Y_1[i]) + ',' + str(Area) + '\r\n')
    # drawing detected table
    #for i in range(len(final_table)):
    #    for j in range(3):
    #        draw_image.rectangle([final_table[i][0]+j, final_table[i][1]+j,
    #                              final_table[i][2]+j, final_table[i][3]+j], fill = None, outline = (255, 0 , 0))
    #    coord = table_coord_actual[i]
        #Area2 = (( coord[0] - coord[2] ) * ( coord[1] - coord[3] )) 
        #file.write ('Detected' + ',' + str(coord[0]) + ',' + str(coord[1]) + ',' + str(coord[2]) 
        #	+ ',' + str(coord[3]) + ',' + str(Area2) + '\r\n')
    #im.save(write_path + "\\" + name_of_file + "_accuracy.png")
    #file.close()

    ## drawing detected table
    #draw_image.rectangle(final_table, fill = None, outline = (255, 0 , 0))
    #coord = final_table
    #Area2 = (( coord[0] - coord[2] ) * ( coord[1] - coord[3] )) 
    ##file.write ('Detected' + ',' + str(coord[0]) + ',' + str(coord[1]) + ',' + str(coord[2]) 
    ##    + ',' + str(coord[3]) + ',' + str(Area2) + '\r\n')
    #im.save(write_path + "\\" + name_of_file + "_accuracy.png")
    ##file.close()

     #call to function of calculating Y cut
    #ar = UT.calc_y_cut(img, final_table, write_path + "\\" + name_of_file + "_column.png")
    
    #UT.calc_accuracy(X, X_1, Y, Y_1, final_table, img, write_path, name_of_file, no_of_table)
    
    # Extracting words of detected table region and writing them to csv
   # UT.extract_table_words(write_path,name_of_file,final_table,arr_of_objects)
    # cal cal_accuracy function
   # UT.cal_accuracy(final_table, X, X_1, Y, Y_1, arr_of_objects, no_of_table, write_path + "\\" + name_of_file + "_Accuracy.csv",write_path,name_of_file)
    # Call confusion matrix 
    #UT.confusion_matrix(X,X_1,Y,Y_1,final_table,img,write_path,name_of_file,no_of_table,arr_of_objects)
    # cal cal_accuracy function
    UT.calc_accuracy(X, X_1, Y, Y_1, final_table,  img, write_path , name_of_file , no_of_table, arr_of_objects)
    # Detect words in the table
    #cells_arr = structure_identification.detecting_cell(img, s_arr,
    #                                                    write_path + "\\" 
    #                                                    + name_of_file + "_cells.png",
    #                                                    table_coord) 
    ## Detect rows in the table
    #structure_identification.detect_rows(img, cells_arr, write_path + "\\" 
    #                                                    + name_of_file  + "_rows.png")
    ## Detecting the cells, rows, columns and tables
    #structure_identification.detect_components(img, cells_arr, write_path + "\\" 
    #                                                    + name_of_file +
    #                                           "_struct_identification.png")
    # Writing the objects to csv for use it for training
    #Writing CSV for cross checking the training result after enhancement in ground truth
    #document_parser.write_to_csv_gt(p_arr, write_path+ "\\" + name_of_file + "_csv_after")
    #document_parser.write_to_csv(array_of_objects, write_path + "\\" + name_of_file)
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



