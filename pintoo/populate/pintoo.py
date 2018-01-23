from populate import base
from main.models import Pintoo, Transport
from django.contrib.auth.models import User



pintoos = ['300片', '500片', '1000片']
transports = ['黑貓宅即便', '超商到店付款']


def populate():
    print('Populating Pintoo ... ', end='')
    Pintoo.objects.all().delete()
    for pintoo in pintoos:
        s = Pintoo()
        s.pintoo = pintoo
        s.save()
    print('done')
    print('Populating Transport ... ', end='')
    for transport in transports:
        s = Transport()
        s.transport = transport
        s.save
    print('done')
    
if __name__ == '__main__':
    populate()