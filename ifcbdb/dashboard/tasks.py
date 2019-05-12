from celery import shared_task

from django.core.cache import cache

from ifcb.viz.mosaic import Mosaic

@shared_task
def mosaic_coordinates_task(bin_id, shape=(600,800), scale=0.33, cache_key=None):
    from dashboard.models import Bin
    h, w = shape
    bin = Bin.objects.get(pid=bin_id)
    b = bin._get_bin()
    m = Mosaic(b, shape=shape, scale=scale)
    print('computing mosaic coordinates for {}'.format(b))
    coordinates = m.pack()
    result = coordinates.to_dict('list')
    cache.set(cache_key, result)
    return result
