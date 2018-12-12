import datetime as dt
from statistics import median
from typing import Optional
import datetime
from api import get_friends
from api_models import User

user_id = int(input('Enter user id: '))

def age_predict(user_id: int) -> Optional[float]:

    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"

    dates = []
    ages = []
    data = get_friends(user_id, 'bdate')
    for i in data['response']['items']:
        if i.get('bdate'):
            dates.append(i['bdate'])

    withyear = []
    for elem in dates:
        if len(elem) in range(8, 11):
            withyear.append(elem)
    dates = withyear

    for elem in dates:
        a = list(map(int, elem.split('.')))
        data = datetime.date(a[2], a[1], a[0])
        age = (datetime.date.today() - data).days // 365
        ages.append(age)
        
    if ages:
        ages.sort()
        if len(ages) % 2 == 1:
            return ages[len(ages) // 2]
        else:
            return (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
    else:
        return None

if __name__ == '__main__':
    print('Age:', age_predict(user_id))
