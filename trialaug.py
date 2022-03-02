from ProAug import Augs
from pprint import pprint
print(Augs.init(dataset_size=10000, total_epochs=100, batch_size=256, lamda=5))
pprint(Augs.show())
pprint (Augs.probability())
pprint ("Choosing Random List: ",Augs.choose_random(91))
pprint (Augs.operator("blur").probability)
pprint (Augs.frequency())
for key, value in Augs.show().items():
    pprint (Augs.operator(key).params.list())
for i in range(5):
    for j in range(1,21):
        for k in range(781):
            Augs.apply_random(1,i*20+j)
    print(Augs.probability())


def doMap(List, n):
    with Pool(n) as p:
        for i in range(6):
            List = p.map(functools.partial(imaugs.scale, factor = 2), List)
        # List = p.map(functools.partial(imaugs.shuffle_pixels, factor = 0.2), List)
        # List = p.map(functools.partial(imaugs.rotate, degrees = 150), List)
        # List = p.map(functools.partial(imaugs.opacity, level=0.8), List)
        # List = p.map(functools.partial(imaugs.hflip, **{}), List)
        # List = p.map(functools.partial(imaugs.shuffle_pixels, factor = 0.0), List)
        # List = p.map(functools.partial(imaugs.shuffle_pixels, factor = 0.0), List)

    return List