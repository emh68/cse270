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
    # Rule 1, pronoun he or she then 's' added to verb
    test_sentence = ["he", "often","talk", "about", "the", "beautiful","house", "along", "the", "quiet", "river" ]
    fix_agreement(test_sentence)
    assert test_sentence[2] == "talks", "The verb should end with 's'."

    # Rule 1, if pronoun not he or she verb does not change
    test_sentence = ["they", "quickly", "walk", "by", "the", "tall", "tree", "beneath", "the", "bright", "moon"]
    fix_agreement(test_sentence)
    assert test_sentence[2] == "walk", "No 's' should be added to the verb."

    # Rule 2, if article 'a' is used and noun two words ahead starts with a vowel, replace article with 'an'
    test_sentence = ["a", "big", "ocean", "quietly", "sleep", "beneath", "the", "bright", "moon"]
    fix_agreement(test_sentence)
    assert test_sentence[0] == "an", "Article did not change to 'an' as expected."
    
    # Rule 2, if article 'a' is used and noun two words ahead does not start with a vowel, article does not change
    test_sentence = ["a", "big", "dog", "quickly", "run", "around", "the", "tree", "by", "the", "river"]
    fix_agreement(test_sentence)
    assert test_sentence[0] == "a", "Article incorrectly changed to 'an'."

    # Rule 3, if sentence starts with 'the' add 's' to the end of verb four words ahead
    test_sentence = ["the", "small", "bird", "happily", "sing", "in", "the", "tall", "tree"]
    fix_agreement(test_sentence)
    assert test_sentence[4] == "sings", "The verb should end with 's'."

    # Rule 3, if sentence does not start with 'the' verb four words ahead does not change
    test_sentence = ["a", "small", "bird", "happily", "play", "in", "the", "tall", "tree"]
    fix_agreement(test_sentence)
    assert test_sentence[4] == "play", "No 's' should be added to the verb."

def test_build_sentence(mocker):
    seed_word = "BAGGAGE"
    structure = ["PRO","ADV","VERB","ART","ADJ","NOUN","PREP","ART","ADJ","NOUN"]
    data = {
        "pronouns": ["I", "you", "he", "she", "we", "they", "it"],
        "nouns": ["dog", "cat", "tree", "house", "ball", "car", "flower"],
        "verbs": ["run", "jump", "sleep", "play", "eat", "dance", "sing"],
        "adjectives": ["big", "small", "happy", "quiet", "fast", "bright", "sad"],
        "adverbs": ["quickly", "happily", "quietly", "slowly", "loudly", "softly", "rarely"],
        "prepositions": ["in", "on", "by", "under", "over", "through", "with"]
    }

    # Mocks random.choice to return first item for deterministic result
    mocker.patch("random.choice", return_value=data["pronouns"][0])

    sentence = build_sentence(seed_word, structure, data)

    assert isinstance(sentence, str), "Sentence should be a string"
    assert sentence[0].isupper(), "Sentence should start with a capital letter"
    assert len(sentence.split()) == len(structure), "Sentence word count should match structure"

