##############################################################################################
# Adding set of the modules important for this class

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image, ImageDraw

class StructureIdentification(object):
    """Class for drawing a structure for table, word, column etc."""

    ###########################################################################################
    # Function for detecting first element in the table

    def detect_first_element_of_table(self, img, arr):
        x_0 = []
        y_0 = []
        width_0 = []
        height_0 = []
        current_value = -1
        if (arr[0].prediction == 1):
                x_0.append(arr[0].x)
                y_0.append(arr[0].y)
                width_0.append(arr[0].width)
                height_0.append(arr[0].height)
                current_value = current_value + 1
        for i in range(0, len(arr)):        
            if (i + 1 < len(arr)):
                if (len(x_0) > 0):
                    if ((arr[i].prediction == 1) and (arr[i].x < x_0[current_value])):
                        x_0[current_value] = arr[i].x
                if ((arr[i].prediction == 0) and (arr[i + 1].prediction == 1)):
                    x_0.append(arr[i + 1].x)
                    y_0.append(arr[i + 1].y)
                    width_0.append(arr[i + 1].width)
                    height_0.append(arr[i + 1].height)
                    current_value = current_value + 1
        return x_0, y_0, width_0, height_0
    
    ###########################################################################################
    # Function for detecting last element in the table

    def detect_last_element_of_table(self, img, arr):
        x_0 = []
        y_0 = []
        width_0 = []
        height_0 = []
        right_extreme_x = 0
        right_extreme_width = 0
        table_existed_ever = False
        if (arr[0].prediction == 1):
            table_existed_ever = True
        for i in range(0, len(arr)):
            if (i + 1 < len(arr)):
                if ((arr[i].prediction == 1)):
                    if (arr[i].x > right_extreme_x):
                        right_extreme_x = arr[i].x 
                        right_extreme_width = arr[i].width              
                if ((arr[i].prediction == 0) and (arr[i + 1].prediction == 1)):
                    table_existed_ever = True
                if ((arr[i].prediction == 1) and (arr[i + 1].prediction == 0)):
                    x_0.append(right_extreme_x)
                    y_0.append(arr[i].y)
                    width_0.append(right_extreme_width)
                    height_0.append(arr[i].height)
                    right_extreme_x = 0
                    right_extreme_width = 0
                    table_existed_ever = False
        if (table_existed_ever == True):
            x_0.append(right_extreme_x)
            y_0.append(arr[len(arr) - 1].y)
            width_0.append(right_extreme_width)
            height_0.append(arr[len(arr) - 1].height)
            table_existed_ever = False

        return x_0, y_0, width_0, height_0
    ###########################################################################################
    # Function for detecting total no of elements in a row of table

    def no_of_words_in_rows(self, arr):
        arr_of_words_in_row_table = []
        index_of_words_in_tables = []
        words_in_row = 0
        i = 0
        index = None
        previous_y = None
        for elements in arr:
            if elements.prediction == 1:
                if (previous_y == None):            
                    previous_y = elements.y
                    words_in_row = words_in_row + 1
                    index_of_words_in_tables.append([])
                    index = 0
                    index_of_words_in_tables[index].append(i)
                elif (elements.y > previous_y):
                    arr_of_words_in_row_table.append(words_in_row)
                    words_in_row = 1
                    previous_y = elements.y
                    index_of_words_in_tables.append([])
                    index = index + 1
                    index_of_words_in_tables[index].append(i)
                elif (elements.y == previous_y):
                    words_in_row = words_in_row + 1
                    index_of_words_in_tables[index].append(i)
            i = i + 1
        arr_of_words_in_row_table.append(words_in_row)
        return arr_of_words_in_row_table, index_of_words_in_tables
          
    ###########################################################################################
    # Function to get the last element column attribute for row detection
    def get_first_element_table_att(self, arr, val):
        x_0 = arr[val].x
        y_0 = arr[val].y
        return x_0, y_0

    ###########################################################################################
    # Function to get the last element column attribute for row detection
    def get_last_element_col_att(self, arr, indexs):
        length = len(indexs)
        x_0 = arr[indexs[length - 1]].x + arr[indexs[length - 1]].width
        y_0 = arr[indexs[length - 1]].y + arr[indexs[length - 1]].height
        return x_0, y_0
    
    ###########################################################################################
    # Function for detecting average distance among rows in y direction

    def avg_dist_row_y(self, arr, val_1, val_2):
        y_dist = abs (arr[val_1].y - arr[val_2].y)
        return y_dist

    ###########################################################################################
    # Drawing the cells, columns, rows and table
    # for post processing
    def detect_tables(self, img, arr, out_img):
        #image = np.array(Image.open(img))
        #fig, ax = plt.subplots(1)
        #ax.imshow(image)
        # Calculating the words in tables in each row and there index
        no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        # Extracting the no of elements from each array
        length_of_no_of_elements = len(no_of_elements)
        last_row = no_of_elements[length_of_no_of_elements - 1]
        second_last_row = no_of_elements[length_of_no_of_elements - 2]
        third_last_row = no_of_elements[length_of_no_of_elements - 3]
        # Calculating the y distances
        second_last_y = self.avg_dist_row_y(arr, index_of_word_in_tables[length_of_no_of_elements - 3][0], index_of_word_in_tables[length_of_no_of_elements - 2][0])
        last_y = self.avg_dist_row_y(arr, index_of_word_in_tables[length_of_no_of_elements - 2][0], index_of_word_in_tables[length_of_no_of_elements - 1][0])
        # removing the extra last row
        if (last_row == 1):
            if (abs(second_last_y - last_y) > 45):
                for elements in index_of_word_in_tables[length_of_no_of_elements - 1]:
                    arr[elements].prediction = 0
        # If the difference between last and second element height is greater than 45 then
        # delete the last row
        if (abs(second_last_y - last_y) > 45):
            for elements in index_of_word_in_tables[length_of_no_of_elements - 1]:
                arr[elements].prediction = 0     
        #######################################################################################
        # drawing box over complete Table
        x_0, y_0, width_0, height_0 = self.detect_first_element_of_table(img, arr)
        x_1, y_1, width_1, height_1 = self.detect_last_element_of_table(img, arr)
        table_coord = []
        table_coord_actual = []
        no = 0
        ########################################################################################
        # PIL way for drawing on the picture
        image = Image.open(img).convert('RGBA')
        draw = ImageDraw.Draw(image)
        for i in range(0, len(x_0)):
            for j in range(0, 4):
                draw.rectangle([x_0[i] + j, y_0[i] + j, x_1[i] + width_1[i] + j, y_1[i] + height_1[i] + j], outline="red")
            print("Detected Table ", i+1," x_0 , y_0, x_1, y_1: ", x_0[i], y_0[i], x_1[i] + width_1[i], y_1[i] + height_1[i])
        #for i in range(0, len(x_0)):
        #    rect = patches.Rectangle((x_0[i], y_0[i]),
        #                             abs(x_1[i] - x_0[i] + width_1[i] + width_1[i]),
        #                             abs(y_1[i] - y_0[i] + height_1[i] + height_1[i]),
        #                             linewidth=1, edgecolor='r',
        #                                       facecolor='none')
            #ax.add_patch(rect)
            table_coord.append([])
            table_coord[no].append(x_0[i])
            table_coord[no].append(y_0[i])
            table_coord[no].append(x_1[i] - x_0[i] + width_1[i])
            table_coord[no].append(y_1[i] - y_0[i] + height_1[i])

            table_coord_actual.append([])
            table_coord_actual[no].append(x_0[i])
            table_coord_actual[no].append(y_0[i])
            table_coord_actual[no].append(x_1[i] + width_1[i])
            table_coord_actual[no].append(y_1[i] + height_1[i])
            no = no + 1

        #plt.savefig(out_img, transparent=True, dpi=300)
        #plt.close()
        image.save(out_img, "PNG", quality=0)
        
        #plt.show()
        return arr, table_coord, table_coord_actual
    #######################################################################################
    # Detecting tables
    def detect_components(self, img, arr, out_img):
        #image = np.array(Image.open(img))
        #fig, ax = plt.subplots(1)
        #ax.imshow(image)
        image = Image.open(img).convert("RGBA")

        # Calculating the words in tables in each row and there index
        no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        # Extracting the no of elements from each array
        length_of_no_of_elements = len(no_of_elements)
        last_row = no_of_elements[length_of_no_of_elements - 1]
        second_last_row = no_of_elements[length_of_no_of_elements - 2]
        third_last_row = no_of_elements[length_of_no_of_elements - 3]
        # Calculating the y distances
        second_last_y = self.avg_dist_row_y(arr, index_of_word_in_tables[length_of_no_of_elements - 3][0], index_of_word_in_tables[length_of_no_of_elements - 2][0])
        last_y = self.avg_dist_row_y(arr, index_of_word_in_tables[length_of_no_of_elements - 2][0], index_of_word_in_tables[length_of_no_of_elements - 1][0])
        # removing the extra last row
        if (last_row == 1):
            if (abs(second_last_y - last_y) > 45):
                for elements in index_of_word_in_tables[length_of_no_of_elements - 1]:
                    arr[elements].prediction = 0
        # If the difference between last and second element height is greater than 45 then
        # delete the last row
        if (abs(second_last_y - last_y) > 45):
            for elements in index_of_word_in_tables[length_of_no_of_elements - 1]:
                arr[elements].prediction = 0

        #######################################################################################
        # drawing box over complete Table
        x_0, y_0, width_0, height_0 = self.detect_first_element_of_table(img, arr)
        x_1, y_1, width_1, height_1 = self.detect_last_element_of_table(img, arr)
        table_coord = []
        no = 0
        draw = ImageDraw.Draw(image)
        for i in range(0, len(x_0)):
            for j in range(0, 4):
               draw.rectangle([x_0[i] + j, y_0[i] + j, x_1[i] + width_1[i] + j, y_1[i] + height_1[i] + j], outline="red")
        #for i in range(0, len(x_0)):
        #    rect = patches.Rectangle((x_0[i], y_0[i]),
        #                             abs(x_1[i] - x_0[i] + width_1[i]) + width_1[i],
        #                             abs(y_1[i] - y_0[i] + height_1[i] + height_1[i]),
        #                             linewidth=1, edgecolor='r',
        #                                       facecolor='none')
        #    ax.add_patch(rect)
            table_coord.append([])
            table_coord[no].append(x_0[i])
            table_coord[no].append(y_0[i])
            table_coord[no].append(x_1[i] - x_0[i] + width_1[i])
            table_coord[no].append(y_1[i] - y_0[i] + height_1[i])
            no = no + 1
        
        #######################################################################################
        # drawing box over complete row
        no_tables = len(table_coord)
        g_x = []
        g_y = []
        s_x = []
        s_y = []
        
        # get the table coordinates in an array for mapping it further
        # g stands for greater while s stands for smaller
        for x in range(0, no_tables):
            for y in range(0, 4):
                if (y == 0):
                    g_x.append(table_coord[x][y])
                elif (y == 1):
                    g_y.append(table_coord[x][y])
                elif (y == 2):
                    s_x.append(table_coord[x][y])
                elif (y == 3):
                    s_y.append(table_coord[x][y])

        #for x in range(0, len(g_x)):
        #    for i in range(len(arr)):
        #        if(arr[i].prediction == 1):
        #           x_0 = arr[i].x
        #           y_0 = arr[i].y
        #           x_1 = arr[i].width
        #           y_1 = arr[i].height
        #           rect = patches.Rectangle((x_0, y_0), x_1, y_1, linewidth=1, edgecolor='y',
        #                                           facecolor='none')
        #           ax.add_patch(rect)
        #        elif (g_x[x] <= arr[i].x <= s_x[x]) and (g_y[x] <= arr[i].y <= s_y[x]):
        #            arr[i].prediction = 1
        #            x_0 = arr[i].x
        #            y_0 = arr[i].y
        #            x_1 = arr[i].width
        #            y_1 = arr[i].height
        #            rect = patches.Rectangle((x_0, y_0), x_1, y_1, linewidth=1, edgecolor='y',
        #                                             facecolor='none')
        #            ax.add_patch(rect)
        for x in range(0, len(g_x)):
            for i in range(len(arr)):
                if(arr[i].prediction == 1):
                   x_0 = arr[i].x
                   y_0 = arr[i].y
                   x_1 = arr[i].width + x_0
                   y_1 = arr[i].height + y_0
                   for j in range(0, 4):
                        draw = ImageDraw.Draw(image)
                        draw.rectangle([x_0 + j, y_0 + j, x_1 + j, y_1 + j], outline="green")
                elif(g_x[x] <= arr[i].x <= s_x[x]) and (g_y[x] <= arr[i].y <= s_y[x]):
                    arr[i].prediction = 1
                    x_0 = arr[i].x
                    y_0 = arr[i].y
                    x_1 = arr[i].width
                    y_1 = arr[i].height
                    for j in range(0, 4):
                        draw = ImageDraw.Draw(image)
                        draw.rectangle([x_0 + j, y_0 + j, x_1 + j, y_1 + j], outline="green")
        #######################################################################################
        # drawing box over complete row
        no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        # extracting the no of elements from each array
        length_of_no_of_elements = len(no_of_elements)
        # Calculating the words in tables in each row and there index
        no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        draw = ImageDraw.Draw(image)
        for i in range(0, len(index_of_word_in_tables)):        
            t_x_0, t_y_0 = self.get_first_element_table_att(arr,
                                                            index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i][0])
            t_width, c_height = self.get_last_element_col_att(arr,
                                                              index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i])
            for j in range(0, 4):
                        draw.rectangle([t_x_0 + j, t_y_0 + j, t_width + j, c_height + j], outline="blue")        

        image.save(out_img, "PNG", quality=0)

        #no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        ## extracting the no of elements from each array
        #length_of_no_of_elements = len(no_of_elements)
        ## Calculating the words in tables in each row and there index
        #no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        #for i in range(0, len(index_of_word_in_tables)):        
        #    t_x_0, t_y_0 = self.get_first_element_table_att(arr,
        #                                                    index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i][0])
        #    t_width, c_height = self.get_last_element_col_att(arr,
        #                                                      index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i])
        #    rect = patches.Rectangle((t_x_0, t_y_0),
        #                                 abs(t_x_0 - t_width),
        #                                 abs(t_y_0 - c_height),
        #                                 linewidth=0.5, edgecolor='g',
        #                                           facecolor='none')
        #    ax.add_patch(rect)

        #plt.savefig(out_img, transparent=True, dpi=300)
        #plt.close()
        
        #plt.show()
        return


    #######################################################################################
    # Drawing the cells, columns, rows and table for post processing
    def detecting_cell(self, img, arr, out_img, table_coord):
        no_of_tables = len(table_coord)
        g_x = []
        g_y = []
        s_x = []
        s_y = []
        image = Image.open(img).convert('RGBA')
        #image = np.array(Image.open(img))
        #fig, ax = plt.subplots(1)
        #ax.imshow(image)
        # get the table coordinates in an array for mapping it further
        # g stands for greater while s stands for smaller
        for x in range(0, no_of_tables):
            for y in range(0, 4):
                if (y == 0):
                    g_x.append(table_coord[x][y])
                elif (y == 1):
                    g_y.append(table_coord[x][y])
                elif (y == 2):
                    s_x.append(table_coord[x][y])
                elif (y == 3):
                    s_y.append(table_coord[x][y])

        for x in range(0, len(g_x)):
            for i in range(len(arr)):
                if(arr[i].prediction == 1):
                   x_0 = arr[i].x
                   y_0 = arr[i].y
                   x_1 = arr[i].width + x_0
                   y_1 = arr[i].height + y_0
                   for j in range(0, 4):
                        draw = ImageDraw.Draw(image)
                        draw.rectangle([x_0 + j, y_0 + j, x_1 + j, y_1 + j], outline="green")
                elif (g_x[x] <= arr[i].x <= s_x[x]) and (g_y[x] <= arr[i].y <= s_y[x]):
                    arr[i].prediction = 1
                    x_0 = arr[i].x
                    y_0 = arr[i].y
                    x_1 = arr[i].width
                    y_1 = arr[i].height
                    for j in range(0, 4):
                        draw = ImageDraw.Draw(image)
                        draw.rectangle([x_0 + j, y_0 + j, x_1 + j, y_1 + j], outline="green")


        image.save(out_img, "PNG", quality=0)
        #for x in range(0, len(g_x)):
        #    for i in range(len(arr)):
        #        if(arr[i].prediction == 1):
        #           x_0 = arr[i].x
        #           y_0 = arr[i].y
        #           x_1 = arr[i].width
        #           y_1 = arr[i].height
        #           rect = patches.Rectangle((x_0, y_0), x_1, y_1, linewidth=1, edgecolor='g',
        #                                           facecolor='none')
        #           ax.add_patch(rect)
        #        elif (g_x[x] <= arr[i].x <= s_x[x]) and (g_y[x] <= arr[i].y <= s_y[x]):
        #            arr[i].prediction = 1
        #            x_0 = arr[i].x
        #            y_0 = arr[i].y
        #            x_1 = arr[i].width
        #            y_1 = arr[i].height
        #            rect = patches.Rectangle((x_0, y_0), x_1, y_1, linewidth=1, edgecolor='g',
        #                                             facecolor='none')
        #            ax.add_patch(rect)


        #plt.savefig(out_img, transparent=True, dpi=300)
        #plt.close()
        return arr



    ############################################################################
    ## detecting the rows
    def detect_rows(self, img, arr, out_img):
        image = Image.open(img).convert('RGBA')
        #image = np.array(Image.open(img))
        #fig, ax = plt.subplots(1)
        #ax.imshow(image)
        # calculating the words in tables in each row and there index
        no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        # extracting the no of elements from each array
        length_of_no_of_elements = len(no_of_elements)
        # Calculating the words in tables in each row and there index
        no_of_elements, index_of_word_in_tables = self.no_of_words_in_rows(arr)
        for i in range(0, len(index_of_word_in_tables)):        
            t_x_0, t_y_0 = self.get_first_element_table_att(arr, index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i][0])
            t_width, c_height = self.get_last_element_col_att(arr, index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i])
            for j in range(0, 4):
                        draw = ImageDraw.Draw(image)
                        draw.rectangle([t_x_0 + j, t_y_0 + j, t_width + j, c_height + j], outline="blue") 
        image.save(out_img, "PNG", quality=0)    
        #for i in range(0, len(index_of_word_in_tables)):        
        #    t_x_0, t_y_0 = self.get_first_element_table_att(arr, index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i][0])
        #    t_width, c_height = self.get_last_element_col_att(arr, index_of_word_in_tables[length_of_no_of_elements - length_of_no_of_elements + i])
        #    rect = patches.Rectangle((t_x_0, t_y_0),
        #                                 abs(t_x_0 - t_width),
        #                                 abs(t_y_0 - c_height),
        #                                 linewidth=1, edgecolor='b',
        #                                           facecolor='none')
        #    ax.add_patch(rect)
        #plt.savefig(out_img, transparent=True, dpi=300)
        #plt.close()    
##############################################################################################
########################################END###################################################
##############################################################################################