import main
import requests
import pytest




def test_response():
   url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
   response = requests.get(url)
   assert response.status_code == 200
   assert response.headers['Content-Type'] == 'application/json; charset=utf-8'



@pytest.mark.parametrize(
        ["height", "measur", "res"],
        [
            (1, 'cm', 1),
            (5, 'meters', 500)
        ]
)
def test_height_calculator(height, measur, res):
   assert main.height_calculator(height, measur) == res



@pytest.mark.parametrize(
        ["occupation", "res"],
        [
            ('-', False),
            ('Any text', True)
        ]
)
def test_work_status(occupation, res):
   assert main.work_status(occupation) == res



@pytest.mark.parametrize(
        ["gender", "work", 'res'],
        [
            ('Male', True, 'Male'),
            ('Male', False, 'Male'),
            ('Female', True, 'Female'),
            ('Female', False, 'Female')
        ]
)
def test_your_superhero(gender, work, res):
   assert main.your_superhero(gender, work)['appearance']['gender'] == res



@pytest.mark.parametrize(
        ["gender", "work"],
        [
            ('Male', 'True'),
            ('Boy', True)
        ]
)
def test_your_superhero_invalid_data(gender, work):
   with pytest.raises(TypeError, match="Ошибка входных данных"):
      main.your_superhero(gender, work)
