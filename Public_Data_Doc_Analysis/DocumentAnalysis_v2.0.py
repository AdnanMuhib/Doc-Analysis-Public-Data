##############################################################################################
# Adding set of the modules important for this class
import DocumentParser as DP
"""Its basically document analysis interface for creation of dataset and feature extraction.
    (Updated 18/4/17)"""

import DataCollector as DC
import FeatureExtraction as FE
import os
import re

##############################################################################################
# Main function for document analysis

def main(table, img, ocr, name_of_file):
    # Creating instances for cross library work
    document_parser = DP.DocumentParser()
    feature_extractor = FE.FeatureExtraction()
    # Read table xml file and  calculate the line spaces
    no_of_table, X, Y, X_1, Y_1, width, height = document_parser.table_to_array(table)
    # Read the word list xml file
    no_of_words, total_width, total_height, words, word_X, word_Y, word_Width, word_Height\
        = document_parser.word_to_array(ocr)
    # Assigning values to struct object and creating an array.  this is array is basically
    # An array of objects
    arr_of_objects = feature_extractor.assigning_values_to_the_struct(no_of_words, word_X,
                                                                      word_Y, word_Width,
                                                                      word_Height, words, 
                                                                      X, Y, X_1, Y_1)
    # Sorting an array because initially its not in order
    sorted_array_y = feature_extractor.sort_array(arr_of_objects)
    # There is a difference in different words vertically in a line.  So eliminating that
    # difference to sort perfectly
    eliminated_diff = feature_extractor.eliminate_y_diff(sorted_array_y)
    # After sorting y then we need to sort every x in that specific y
    sorted_array_x = feature_extractor.sort_array_by_x(eliminated_diff)
    # Distance is then calculated between words for training purpose
    dist_calculted_arr = feature_extractor.calculate_dist(sorted_array_x)
    # Now the list of objects are stored in an array for writing it into csv
    array_of_objects = feature_extractor.objects_to_array(dist_calculted_arr)
    # Writing the objects to csv for use it for training
    document_parser.write_to_csv(array_of_objects, name_of_file)
    #document_parser.write_to_arff(arr_of_objects, name_of_file)
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
        main(table, img, ocr, file_to_write)

    # end of the batch processing
    return



##############################################################################################
# Magic Lines

if __name__ == "__main__":
    batch_processor()


##############################################################################################
########################################END###################################################
##############################################################################################
