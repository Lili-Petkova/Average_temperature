from aiohttp import ClientSession
import asyncio

site_1 = 'https://api.open-meteo.com/v1/forecast?latitude=49.988358&longitude=36.232845&current_weather=True'
site_2 = 'https://www.7timer.info/bin/astro.php?lon=36.232845&lat=49.988358&ac=0&unit=metric&output=json&tzshift=0'
site_3 = 'http://t.weather.sojson.com/api/weather/city/101030100'


async def site_meteo(site, session):
    async with session.get(site) as response:
        if response.status == 200:
            print(f'{site_1}')
            data = await response.json()
            temperature = data['current_weather']['temperature']
    return temperature


async def site_seventimer(site, session):
    async with session.get(site) as response:
        if response.status == 200:
            print(f'{site_2}')
            data = await response.json(content_type='text/html')
            temperature = data['dataseries'][0]['temp2m']
    return temperature


async def site_goweather(site, session):
    async with session.get(site) as response:
        if response.status == 200:
            print(f'{site_3}')
            data = await response.json()
            temperature = data['data']['pm25']
    return temperature


async def main():
    async with ClientSession() as session:
        result = await asyncio.gather(site_meteo(site_1, session), site_seventimer(site_2, session),
                                      site_goweather(site_3, session))
        average_temperature = round(sum(result) / len(result), 2)
    return average_temperature


if __name__ == '__main__':
    print('THE WEATHER INFO')
    print('Information taken from these sites:')
    print(f'For today the average temperature is {asyncio.run(main())} °C')
