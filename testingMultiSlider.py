import npyscreen


class MultiSlider(npyscreen.MultiLine):
	_contained_widgets = npyscreen.Slider

        def display_value(self, vl):
                return float(vl)

def main(screen):
        F = npyscreen.Form()
        ms3= F.add(MultiSlider)
        ms3.values = [
						1, 10, 5, 20, 2, 30, 29, 22, 21, 18,
						1, 10, 5, 20, 2, 30, 29, 22, 21, 18,
						1, 10, 5, 20, 2, 30, 29, 22, 21, 18,
                     ]
        F.edit()

if __name__ == '__main__':
	npyscreen.wrapper(main)
