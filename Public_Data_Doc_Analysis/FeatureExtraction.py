############################################################################################
# Adding set of the modules important for this class
import math
import DataCollector as DC

class FeatureExtraction(object):
    """A class for feature extraction assigning values to the struct, calculating distances,
    elimation differences and sorting the array.
    (Updated 18/4/17)"""

    ########################################################################################
    # Adding set of the modules important for this class

    def assigning_values_to_the_struct(self, no_of_words, word_X, word_Y, word_Width, 
                                       word_Height, words, X, Y, X_1, Y_1):
        arr_of_objects = []
        for x in range(0, no_of_words):
            arr_of_objects.append(DC.DataCollector(word_X[x], word_Y[x],
                        word_Width[x],
                        word_Height[x],
                        words[x], self.part_of_table(word_X[x], word_Y[x], X, Y, X_1,
                                                     Y_1)))
        return arr_of_objects

    ########################################################################################
    # Checking whether part of the table or not

    def part_of_table(self, x, y, X, Y, X_1, Y_1):
        table = 0
        for i in range(0, len(X)):
            if ((X[i] <= x <= X_1[i]) and (Y[i] <= y <= Y_1[i])):
                table = 1
            else: table = 0
        return table


    ########################################################################################
    # Sorting the array of objects with respect to y values
    def sort_array(self, new_array_of_objects):
        changed = True
        while changed:
            changed = False
            for i in range(len(new_array_of_objects) - 1):
                if new_array_of_objects[i].y > new_array_of_objects[i+1].y:
                    new_array_of_objects[i], new_array_of_objects[i+1] = new_array_of_objects[i+1], new_array_of_objects[i]
                    changed = True
        return new_array_of_objects

    ########################################################################################
    # Sorting the y values sorted array of objects with respect to x values
    def sort_array_by_x(self, new_sorted_array):
        changed = True
        while changed:
            changed = False
            for i in range(len(new_sorted_array) - 1):
                if new_sorted_array[i].y == new_sorted_array[i+1].y:
                    if new_sorted_array[i].x > new_sorted_array[i+1].x:
                        new_sorted_array[i], new_sorted_array[i+1] = new_sorted_array[i+1], new_sorted_array[i]
                        changed = True
        return new_sorted_array


    ########################################################################################
    # There is difference in pixels values along the y axis because of raw data to remove 
    # that difference you can simply change the value of 20 to the required one
    
    def eliminate_y_diff(self, arr):
        previous_y = arr[0].y
        for i in range(len(arr)):
            if(i != len(arr) - 1):
                if(abs(arr[i].y - previous_y) < 20):
                    arr[i].y = previous_y
            previous_y = arr[i].y
        return arr

    ########################################################################################
    # Calculating distances among the x, y elements

    def calculate_dist(self, my_sorted_array):
        # by using the formula distance=sqrt((x2-x1)^2+(y2-y1)^2))
        # x+1 and x-1 distance
        for i in range(len(my_sorted_array)):
            if i == 0:
                my_sorted_array[i].x_1_dist = math.ceil(math.sqrt(pow((\
                    my_sorted_array[i + 1].x-my_sorted_array[i].x),2) +
                                                          pow( (my_sorted_array[i+1].y\
                                                              - my_sorted_array[i].y),2)))
                my_sorted_array[i].x_m_1_dist= 0
            elif(i == len(my_sorted_array)-1):
                my_sorted_array[i].x_1_dist= 0
                my_sorted_array[i].x_m_1_dist = math.ceil(math.sqrt(pow((\
                    my_sorted_array[i].x - my_sorted_array[i-1].x),2) + pow((\
                    my_sorted_array[i].y - my_sorted_array[i-1].y), 2)))
            else:
                my_sorted_array[i].x_1_dist= math.ceil(math.sqrt(pow((\
                    my_sorted_array[i + 1].x - my_sorted_array[i].x),2) + pow((\
                    my_sorted_array[i + 1].y - my_sorted_array[i].y),2)))
                my_sorted_array[i].x_m_1_dist=math.ceil(math.sqrt(pow((\
                    my_sorted_array[i].x - my_sorted_array[i-1].x), 2) +  pow((\
                    my_sorted_array[i].y - my_sorted_array[i-1].y), 2)))
        # for y+1 and y-1 distance
        words_in_row = 0
        total_words = 0
        line_index=0
        y_m_1_dist = 0
        row_y_position=my_sorted_array[0].y
        row_x_position=my_sorted_array[0].x
        for i in range ( len(my_sorted_array) ):
            total_words += 1
            if row_y_position == my_sorted_array[i].y:
                words_in_row += 1
                my_sorted_array[i].y_m_1_dist = y_m_1_dist
            else:
                #print("Total Words in the row are : ",words_in_row_counter)
                y_m_1_dist = math.ceil(math.sqrt(pow((my_sorted_array[i].x -\
                   row_x_position), 2) + pow((my_sorted_array[i].y - \
                   row_y_position), 2)))
                row_y_position = my_sorted_array[i].y
                row_x_position = my_sorted_array[i].x
                for j in range(line_index, (line_index + words_in_row)):
                    my_sorted_array[j].y_1_dist = y_m_1_dist
                line_index=total_words
                my_sorted_array[i].y_m_1_dist = y_m_1_dist
                my_sorted_array[i].y_1_dist = y_m_1_dist
                words_in_row=0
        return my_sorted_array

    ########################################################################################
    # Copying all the objects value to an array for further writing it to the csv file

    def objects_to_array(self, arr):
        return_arr = []
        return_arr.append([])
        return_arr[0].append("word")
        return_arr[0].append("x")
        return_arr[0].append("y")
        return_arr[0].append("x+1 dist")
        return_arr[0].append("x-1 dist")
        return_arr[0].append("y+1 dist")
        return_arr[0].append("y-1 dist")
        return_arr[0].append("width")
        return_arr[0].append("height")
        return_arr[0].append("table")

        index = 1
        for i in range(0, len(arr)):
            return_arr.append([])
            return_arr[index].append(arr[i].word)
            return_arr[index].append(arr[i].x)
            return_arr[index].append(arr[i].y)
            return_arr[index].append(arr[i].x_1_dist)
            return_arr[index].append(arr[i].x_m_1_dist)
            return_arr[index].append(arr[i].y_1_dist)
            return_arr[index].append(arr[i].y_m_1_dist)
            return_arr[index].append(arr[i].width)
            return_arr[index].append(arr[i].height)
            return_arr[index].append(arr[i].table)
            index = index + 1
        return return_arr

    ########################################################################################
    ##########################################END###########################################
    ########################################################################################


