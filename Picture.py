__author__ = 'mattisaraya'

import Behavior

class Picture(Behavior.Behavior):




     def dominant_color_in_picture(self):  #returnerer den dominerende fargen i et bilde(RGB)

        image=Imager(image=self.get_value())
        image=image.resize(70,70)

        image_width=70
        image_height=70

        R_value=0
        G_value=0
        B_value=0

        self.greatest_color_value=''

        #regner ut gjennomsnittsverdien
        for i in range(0,image_width):
            for x in range(image_height):
                R=image.get_pixel(i,x)
                G=image.get_pixel(i,x)
                B=image.get_pixel(i,x)

                R_value=(R+R_value)/2
                G_value=(G+G_value)/2
                B_value=(B+B_value)/2

        if R_value>=G_value and R_value>=B_value:
            self.greatest_color_value='red'

        elif G_value>=R_value and G_value>=B_value:
            self.greatest_color_value='green'

        elif B_value>=R_value and B_value>=G_value:
            self.greatest_color_value='blue'

        else:
            self.greatest_color_value='undesided'

        return self.greatest_color_value