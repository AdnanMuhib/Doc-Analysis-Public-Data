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

##############################################################################################
# Main function for document analysis
def main(table, img, ocr, name_of_file, arff, out_img):
    # Creating instances for cross library work
    document_parser = DP.DocumentParser()
    feature_extractor = FE.FeatureExtraction()
    weka_machine_learning = WML.WekaMachineLearning()
    structure_identification = Struct_I.StructureIdentification()
    post_processor = PP.PostProcessor()
    cell_drawing = CD.CellDrawing()
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
    # prediction = weka_machine_learning.weka_cross_validation("D:\Adnan\Table Recognition GUI\Model\Model.model", arff)
    # Adding prediction to the array for further easy use
    p_arr = post_processor.prediction_to_array(dist_calculted_arr, prediction)
    # Output look before applying the ground truth
    cell_drawing.draw_prediction(p_arr, img, name_of_file + "_before")
    # Applying ground truth
    n_arr = post_processor.ground_truth_x(p_arr, prediction)
    # Output look like after applying the ground truth
    cell_drawing.draw_prediction(n_arr, img, name_of_file + "_after")
    # Detect table
    s_arr, table_coord = structure_identification.detect_tables(img, n_arr, out_img)
    # Detect words in the table
    cells_arr = structure_identification.detecting_cell(img, s_arr,
                                                        name_of_file + "_cells.png",
                                                        table_coord) 
    # Detect rows in the table
    structure_identification.detect_rows(img, cells_arr, name_of_file + "_rows.png")
    # Detecting the cells, rows, columns and tables
    structure_identification.detect_components(img, cells_arr, name_of_file + "_struct_identification.png")
##############################################################################################
# batch processor for running it in loop over all the lements in that directory
def batch_processor():
    dir_img = "F:\KICS - Research Officer\CVML\Document Analysis\DATA SET\Test Data\Images"
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

##############################################################################################
# For cross compilation
def setup_main(path, file_name, write_path):
	table = path + "//" + file_name + ".xml"
	ocr = path + "//" + file_name + "_ocr.xml"
	img = path + "//" + file_name + ".png"
	arff = path + "//" + file_name + "_arff.arff"
	file_to_write = file_name
	out_image = write_path + "//" + file_name + "_table.png"
	try:
		jvm.start()
		main(table, img, ocr, file_to_write, arff, out_img)
	except Exception, e:
		print(traceback.format_exc())
	finally:
		jvm.stop()
	return


##############################################################################################
# Command line arguments
if __name__ == "__main__":
    print "Hello"
    #path = sys.argv[1]
    #file_name = sys.argv[2]
    #write_path = sys.argv[3]
    #setup_main(path, file_name, write_path)



##############################################################################################
########################################END###################################################
##############################################################################################



