class Zone:
    
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        
    def is_in_zone(self, zone):
        #print(len(zone)) видит
        for i in range(0, len(zone) - 1, 2): # Цикл не запускается (???)
            #print(len(zone)) не видит
            if (self.x1 < zone[i] < self.x2 or self.x3 < zone[i] < self.x4) and (self.y1 < zone[i + 1] < self.y4 or self.y2 < zone[i + 1] < self.y3):
                return True
        return False
    def get_list(self):
        return [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4]