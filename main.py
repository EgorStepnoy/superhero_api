import requests



def height_calculator(height: str, measur: str) -> int | float:
    height = float(height)
    if measur == 'cm':
        return height
    elif measur == 'meters':
        return height * 100
    else:
        return 0


def work_status(occupation: str) -> bool:
    if occupation == '-':
        return False
    else:
        return True


def get_request():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    r = requests.get(url)
    return r.json()


def your_superhero(gender: str, work: bool) -> dict | None:
    if not isinstance(gender, str) or gender.lower() not in ('male', 'female') or not isinstance(work, bool):
        raise TypeError("Ошибка входных данных")
    heroes_list = get_request()
    max_height = -1
    highest_hero = {}
    for hero in heroes_list:
        height, measur = hero['appearance']['height'][1].split()
        occupation = hero['work']['occupation']
        if work_status(occupation) == work and gender.lower() == hero['appearance']['gender'].lower() and height_calculator(height, measur) > max_height:
            max_height = height_calculator(height, measur)
            highest_hero = hero
    if max_height == -1:
        return None
    else:
        return highest_hero