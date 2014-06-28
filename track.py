import pygeoip

print '\t\t\t ######################################'
print '\t\t\t ##    Proudly Made By An INDIAN     ##'
print '\t\t\t ##   Author : Rohit Saxsena INDIA   ##'
print '\t\t\t ######################################'

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def TargetIP(target):
	rec = gi.record_by_name(target)
	city = rec['city']
	region = rec['region_name']
	country = rec['country_name']
	long = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' + target + ' Geo-located. '
	print '[+] Adress: '+str(city)+', '+str(region)+', '+str(country)
	print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)

host = raw_input('Enter Target :')
target = host
TargetIP(target)
