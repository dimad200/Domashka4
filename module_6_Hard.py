class Figure():
    sides_count = 0
    __sides =0
    __color =[0,0,0] #(список цветов в формате RGB)
    filled=False
    def get_color(self):
        pass


    def __is_valid_color(r,g,b):
        if type(r)==int and type(g) ==int and type(b)==int:
            if r>=0 and r<=255 and g>=0 and g<=255 and b>=0 and b<=255:
                return True
        else:                   
            return False        

    def set_color(self, r,g,b):
        pass


sabaren =Figure
sabaren._Figure__is_valid_color(12,12,12)
print(sabaren._Figure__is_valid_color(12,12,20))