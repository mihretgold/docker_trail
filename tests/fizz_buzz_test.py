from .. import main  # Adjust this import based on your actual file names

def test_fizzbuzz():
    result = main.fizzBuzz(15)
    assert result == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz Buzz"]
