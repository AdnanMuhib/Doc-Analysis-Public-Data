class DataCollector(object):
    """A struct method for data storage. It consists of all types of data to be stored in 
    our array of objects. These data types mainly include distances in (x_1_dist, 
    x_m_1_dist, y_1_dist, y_m_1_dist), values of the neighbour in (neighbour_1,
    neighbour_2, neighbour_3, neighbour_4), actual values of that word whether in table or
    not in the data type table and predicted values by weka in prediction.
    (Updated 18/4/17)"""
    ###################################################################################
    # Variable types
    x_1_dist = None
    x_m_1_dist = None
    y_1_dist = None
    y_m_1_dist = None
    
    table = None

    neighbour_1 = None
    neighbour_2 = None
    neighbour_3 = None
    neighbour_4 = None

    prediction = None

    ###################################################################################
    # Initialization function or constructor to be called always when the class is
    # created
    def __init__(self, x, y, width,
                 height, word, table):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = word
        self.table = table
        return
    
    ###################################################################################
    ########################################END########################################
    ###################################################################################


