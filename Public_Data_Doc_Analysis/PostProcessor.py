class PostProcessor(object):
    """Its a class for classification, prediction etc. 
    Updated (19/4/17)"""

    ###########################################################################################
    # adding prediction to the array for further easy use

    def prediction_to_array(self, arr, prediction):
        for i in range(0, len(prediction)):
            if (prediction[i] == "+"):
                if (not(arr[i].table) == False):
                    arr[i].prediction = 0
                elif (not(arr[i].table) == True):
                    arr[i].prediction = 1
            else:
                arr[i].prediction = arr[i].table
        return arr

    ###########################################################################################
    # ground truth improvements for better results

    def ground_truth_x(self, my_sorted_array, wrong_predictions):
        if (len(my_sorted_array) - len(wrong_predictions) == 0):
            length = len(my_sorted_array)
        else:
            length = len(wrong_predictions)
        for i in range(length):
            if (wrong_predictions[i] == "+"):
                if i == 0:
                    my_sorted_array[i].neighbour_1 = my_sorted_array[i + 1].prediction
                    my_sorted_array[i].neighbour_2 = my_sorted_array[i + 2].prediction
                    val = my_sorted_array[i].neighbour_1 and my_sorted_array[i].neighbour_2
                    my_sorted_array[i].prediction = val
                elif(i == len(my_sorted_array) - 1):
                    my_sorted_array[i].neighbour_1 = 0
                    my_sorted_array[i].neighbour_2 = my_sorted_array[i - 1].prediction
                    val = my_sorted_array[i].neighbour_1 and my_sorted_array[i].neighbour_2
                    my_sorted_array[i].prediction = val
                else:
                    my_sorted_array[i].neighbour_1 = my_sorted_array[i - 2].prediction
                    my_sorted_array[i].neighbour_2 = my_sorted_array[i - 1].prediction
                    val = my_sorted_array[i].neighbour_1 and my_sorted_array[i].neighbour_2
                    my_sorted_array[i].prediction = val
        return my_sorted_array

    ##############################################################################################
    ########################################END###################################################
    ##############################################################################################
