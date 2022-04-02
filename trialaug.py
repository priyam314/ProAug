from ProAug import 
from pprint import pprint
print(Augs.init(dataset_size=10000, total_epochs = 10, batch_size=512, lamda=5))
for i in range(50):
    Augs.choose_random(i)
    Augs.update_parameters(i)
pprint(Augs.get_parameters_value("all"))
new = {'blur': {'radius': 41.498945069075848},
 'color_jitter': {'brightness_factor': 6.107177112742326,
                  'contrast_factor': 6.5,
                  'saturation_factor': 5.6},
 'grayscale': {'mode': 'average'},
 'hflip': {},
 'opacity': {'level': 0.8}}
Augs.load_params(new)
pprint(Augs.get_parameters_value("all"))
Augs.choose_random(51)
Augs.update_parameters(51)
pprint(Augs.get_parameters_value("all"))