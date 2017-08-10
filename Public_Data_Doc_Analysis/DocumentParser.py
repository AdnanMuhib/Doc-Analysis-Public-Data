###################################################################################
# Adding set of the modules important for this class
import csv
import numpy as np
from PIL import Image
import xml.dom.minidom as minidom
import math
import unicodedata
import arff

class DocumentParser(object):
    """A Document Analysis class for reading and writing of different formats or types
    present for wordlist, ground truth etc. These type mainly include XML, CSV, ARFFS
    and PNGS.
    (Updated 18/4/17)"""

    ###################################################################################
    # for calculating the width/height of the table
    def calc_difference(self, x0, x1):
        return (x1 - x0)



    ###################################################################################
    # Writing the words from the wordlist to an array

    def word_to_array(self, file):
        no_of_words = 0
        total_width = 0
        total_height = 0
        words = []
        word_X = []
        word_Y = []
        word_Width = []
        word_Height = []
        # Parse the file using element treee for xml parser get the root object to move forward
        root = minidom.parse(file)
        # Get the number of tables
        no_of_words = len(root.getElementsByTagName('word'))
        # Total lenght of document
        for info in root.getElementsByTagName('docinfo'):
            total_width = int(unicodedata.normalize('NFKD', info.getAttribute("width")).encode('ascii', 'ignore'))
            total_height = int(unicodedata.normalize('NFKD',info.getAttribute("height")).encode('ascii', 'ignore'))
        # Get the elements by tag name and store it in an array
        for elements in root.getElementsByTagName('word'):
            _words = str(unicodedata.normalize('NFKD', (elements.childNodes[0].data)).encode('ascii', 'ignore'))
            left = int(unicodedata.normalize('NFKD', (elements.getAttribute("left"))).encode('ascii', 'ignore'))
            right = int(unicodedata.normalize('NFKD', (elements.getAttribute("right"))).encode('ascii', 'ignore'))
            top = int(unicodedata.normalize('NFKD', (elements.getAttribute("top"))).encode('ascii', 'ignore'))
            bottom = int(unicodedata.normalize('NFKD', (elements.getAttribute("bottom"))).encode('ascii', 'ignore'))
            words.append(_words)        
            word_X.append(left)
            word_Y.append(abs(total_height - top))
            word_Width.append(abs(left - right))
            word_Height.append(abs(top - bottom))
        # Removing the new lines tokens
        y = 0
        for word in words:
            words[y] = word.replace("\n", "")
            y = y + 1
        return no_of_words, total_width, total_height, words, word_X, word_Y, word_Width, word_Height

    ###################################################################################
    # Writing the coordinates of the tables from the xml to array of table as ground
    # truth

    def table_to_array(self, file):
        no_of_tables = 0
        X = []
        Y = []
        X_1 = []
        Y_1 = []
        Width = []
        Height = []
        # Parse the file using element treee for xml Parser get the root object to move
        # forward
        root = minidom.parse(file)
        # get the number of tables
        no_of_tables = len(root.getElementsByTagName('Table'))
    
        # Get the elements by tag name and store it in an array
        for elements in root.getElementsByTagName('Table'):
            X.append(int(unicodedata.normalize('NFKD', (elements.getAttribute("x0"))).encode('ascii', 'ignore')))
            Y.append(int(unicodedata.normalize('NFKD', (elements.getAttribute("y0"))).encode('ascii', 'ignore')))
            X_1.append(int(unicodedata.normalize('NFKD', (elements.getAttribute("x1"))).encode('ascii', 'ignore')))
            Y_1.append(int(unicodedata.normalize('NFKD', (elements.getAttribute("y1"))).encode('ascii', 'ignore')))
            Width.append(self.calc_difference(int(unicodedata.normalize('NFKD', (elements.getAttribute("x0"))).encode('ascii', 'ignore')), 
                                             int(unicodedata.normalize('NFKD', (elements.getAttribute("x1"))).encode('ascii', 'ignore'))))
            Height.append(self.calc_difference(int(unicodedata.normalize('NFKD', (elements.getAttribute("y0"))).encode('ascii', 'ignore')), 
                                             int(unicodedata.normalize('NFKD', (elements.getAttribute("y1"))).encode('ascii', 'ignore'))))
        return no_of_tables, X, Y, X_1, Y_1, Width, Height
  
    ###################################################################################
    # Writing the array of objects to arff for weka testing-traing purpose

    def write_to_arff(self, arr, name_of_file):
        return_arr = []  
        index = 0
        name_of_file = name_of_file + "_arff.arff"
        for i in range(0, len(arr)):
            return_arr.append([])
            #return_arr[index].append(arr[i].word)
            #return_arr[index].append(arr[i].x)
            #return_arr[index].append(arr[i].y)
            return_arr[index].append(arr[i].x_1_dist)
            return_arr[index].append(arr[i].x_m_1_dist)
            #return_arr[index].append(arr[i].y_1_dist)
            #return_arr[index].append(arr[i].y_m_1_dist)
            return_arr[index].append(arr[i].width)
            return_arr[index].append(arr[i].height)
            return_arr[index].append(arr[i].table)
            index = index + 1
        # Dump function for dumping values to a file
        arff.dump(name_of_file, return_arr, relation="wordlist",
                  names=["x_1_dist", "x_m_1_dist",
                         "width", "height",
                         "table"])
        return

    ###################################################################################
    # Writing the array of objects to CSV for weka testing-traing purpose or self 
    # evaluation

    def write_to_csv(self, arr, name_of_file):
        name_of_file = name_of_file + '.csv'
        with open(name_of_file, "wb") as f:
            write = csv.writer(f)
            write.writerows(arr)
        return

    ###################################################################################
    # Writing the array of objects to CSV for weka testing-traing purpose or self 
    # evaluation
    def write_to_csv_gt(self, arr, name):
        no_of_words = len(arr)
        #print("table : prediction")
        words_in_table = 0
        words_in_table_dected_non_table = 0
        words_in_non_table = 0
        words_in_non_table_detected_table = 0
        for i in range(0, no_of_words):
            #print(arr[i].table, ":" ,arr[i].prediction)
            if (arr[i].table == 1 and arr[i].prediction == 1):
                words_in_table = words_in_table + 1
            elif (arr[i].table == 0 and arr[i].prediction == 0):
                words_in_non_table = words_in_non_table + 1
            elif (arr[i].table == 1 and arr[i].prediction == 0):
                words_in_table_dected_non_table = words_in_table_dected_non_table + 1
            elif (arr[i].table == 0 and arr[i].prediction == 1):
                words_in_non_table_detected_table = words_in_non_table_detected_table + 1
            elif (arr[i].prediction == None):
                if (arr[i].table == 1):
                    words_in_table = words_in_table + 1
                elif (arr[i].table == 0):
                    words_in_non_table = words_in_non_table + 1
        #print("table : Non Table : wrong Detected Table : wrong Detected Non Table")
        #print(words_in_table, "   ", words_in_non_table, "   ", words_in_non_table_detected_table, "   ", words_in_table_dected_non_table)
        _arr = []
        _arr.append([])
        _arr[0].append("Table")
        _arr[0].append("None Table")
        _arr[0].append("wrong Detected Table")
        _arr[0].append("wrong Detected Non Table")
        _arr.append([])
        _arr[1].append(words_in_table)
        _arr[1].append(words_in_non_table)
        _arr[1].append(words_in_non_table_detected_table)
        _arr[1].append(words_in_table_dected_non_table)
        self.write_to_csv(_arr, name)
        return

    ###################################################################################
    ########################################END########################################
    ###################################################################################
