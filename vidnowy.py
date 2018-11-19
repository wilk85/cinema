import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import os


#4 kina w krakowie krakowplaza, bonarka, kazimierz, zakopianka

driver = webdriver.Chrome( executable_path=r"C:/chromedriver/chromedriver.exe")
driver.set_window_size(400, 400)
driver.set_window_position(-600,0)

# lista wywołan dla kin, wyświetlam ją na ekranie
krakow = ['kazimierz', 'bonarka', 'krakowplaza', 'zakopianka']
print('========================================')
print('Lista kin w krakowie: ' + '\n==========')
print(*krakow, sep=', ')
print('========================================')
print()


# zmieniam link żeby wybrać kino 
def ch_cinema(cinema):
    link = 'https://www.cinema-city.pl/kina/'+cinema+'/'
    # print(link)
    return driver.get(link)

# ch_cinema(sys.argv[1])
ch_cinema(krakow[2])


res = driver.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(res, 'html.parser')


# wyświetlam ile filmów jest dziś odtwarzanych
movies_ct = soup.find_all('div', {'class': 'movie-row'})
print('Ilość filmów wyświetlanych dziś' + ' : ' + str(len(movies_ct)))
print()

# tworzę plik csv z wynikiem

# filepath = os.path.join(os.environ['HOMEPATH'], 'Desktop', 'filmy.csv')
# with open('filepath', wb) as f:
#         csv_writer = csv.writer(f)
#         headers = ['Tytuł', 'Wersja', 'Gatunek', 'Godziny']
#         csv_writer.writerow(headers)

for m in soup.find_all('div', {'class': 'movie-row'}):
    genre = m.find('div', {'class': 'qb-movie-info'})
    title = m.find('a', {'class': 'qb-movie-link'})
    events = m.find('div', {'class': 'events'})
    info = m.find('div', {'class': 'qb-movie-info-column'})
    atag = events.find_all('a', {'class': 'btn-primary'})
    clas1 = events.find('div', {'class': 'type-row'})
    
    
    if 'IMAX' in clas1.text or '3D' in clas1.text:
        clas1.decompose()
    else: 
        print(title.text)
        print(clas1.h5.get_text().replace('•', ':'))
        print(' '.join(genre.text.split()))
        for atag in m.find_all('a', class_='btn btn-sm btn-primary'):
                print(atag.get_text(), end=', ')
        print('''''')
        print()
        
        



driver.quit()
exit()
  





