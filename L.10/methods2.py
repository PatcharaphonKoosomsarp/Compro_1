class Calculate_area:

    def rectangle_area(self, w, h):
        return w * h
    
    @classmethod
    def traingle_area(cls, b, h):
        return 0.5 * b * h
    
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r
    
cal = Calculate_area()
cal_rec = cal.rectangle_area(4, 5)
cal_tra = Calculate_area.traingle_area(4, 5)
cal_cir = Calculate_area.circle_area(4)

print('Rectangle Area = ', cal_rec)
print('Traingle Area = ', cal_tra)
print('Circle Area = ', cal_cir)