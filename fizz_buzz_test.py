from main import fizzBuzz


def test_fizzbuzz():
    result = fizzBuzz(15)
    assert result == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz Buzz"]
