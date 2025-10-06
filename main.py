import sys
from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key='YOUR_API_KEY'
geocoder=OpenCageGeocode(key)
addressfile= 'addresses.txt'


try:
    with open(addressfile,'r', encoding='utf-8') as f:
       count=0
       for line in f:
          address=line.strip()
          results=geocoder.geocode(address, no_annotations='1')
          if results and len(results):
                longitude = results[0]['geometry']['lng']
                latitude  = results[0]['geometry']['lat']
                print(u'%f;%f;%s' % (latitude, longitude, address))
          else:
            sys.stderr.write('not found %s\n' % address)
          if not address:
             continue
          count+=1

except IOError:
  print('Error: File %s does not appear to exist.' % addressfile)
except Exception as ex:
  print(f'Error: {ex}')

