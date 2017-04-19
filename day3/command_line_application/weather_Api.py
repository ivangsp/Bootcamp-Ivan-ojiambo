#program wiill generate the weather of the city
#Enter the city name at the command prompt
import urllib
import sys
def weather(city_name=None):
	
	if city_name is None:
		city_name='kampala'

	city_name = city_name.replace(" ",'%20')
	api_key='95b8f13ab7f6f3d6518f4ccadf4300ae'
	url='http://api.openweathermap.org/data/2.5/weather?q='
	
	data = urllib.urlopen(url+city_name+'&APPID='+api_key)
	print (data.read())

def main():
	if len(sys.argv) > 1:
		weather(sys.argv[1])
	else:
		weather()
if __name__=='__main__':
	main()
	