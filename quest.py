class Quest:
    
    def __init__(self, is_completed, task_text, result_text, item):
        self.__task_text = task_text
        self.__result_text = result_text
        self.__is_completed = is_completed
        self.__finish = False
        self.__item = item
        self.__flag = 0
        
    def get_text(self, inventory, item):
            
        if self.__item | inventory == inventory and self.__flag == 1:
            self.__is_completed = True
            
        if not(self.__is_completed):
            self.__flag = 1
            return self.__task_text
        elif self.__is_completed and self.__finish == False:
            inventory -= self.__item 
            inventory.add(item)
            self.__finish = True
            return self.__result_text
        elif self.__finish == True:
            return self.__result_text