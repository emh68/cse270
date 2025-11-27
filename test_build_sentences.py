import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures, pronouns, articles)

def test_get_seven_letter_word(mocker):
    mock_input = mocker.patch("builtins.input", return_value="stadium")
    result = get_seven_letter_word()
    assert result == "STADIUM"
    mock_input.assert_called_once_with("Please enter a word with at least 7 letters: ")

    mock_input = mocker.patch("builtins.input", return_value="hello")
    with pytest.raises(ValueError):
        get_seven_letter_word()
    
   
def test_parse_json_from_file(tmp_path):
    test_data = {"word": "monkey", "length": 6}
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        json.dump(test_data, f)

    result = parse_json_from_file(file_path)

    assert result == test_data

    # Test FileNotFoundError
    file_path = "nonexistent_file.json"

    with pytest.raises(FileNotFoundError):
        parse_json_from_file(file_path)
    
    #Test JSONDecode Error 
    file_path = tmp_path / "bad.json"
    with open(file_path, "w") as f:
        f.write("not valid json")

    with pytest.raises(json.JSONDecodeError):
        parse_json_from_file(file_path)
        

def test_choose_sentence_structure():
    choice = choose_sentence_structure()
    assert choice in structures

def test_get_pronoun():
    choice = get_pronoun()
    assert choice in pronouns

def test_get_article():
    choice = get_article()
    assert choice in articles

def test_get_word():
    test_list = ["apple", "banana", "cherry"]
    assert get_word("A", test_list) == "apple"
    assert get_word("B", test_list) == "banana"

def test_fix_agreement():
    test_sentence = ["he", "often","talk", "about", "the", "beautiful","house", "along", "the", "quiet", "river" ]
    fix_agreement(test_sentence)
    assert test_sentence[2] == "talks"

def test_build_sentence():
    pass