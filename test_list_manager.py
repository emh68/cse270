from list_manager import (reset_list, get_list, add_to_list, remove_from_list, replace_item_in_list, get_item_at_position)
import pytest

## Ensures the we can get the list in any state
def test_get_list():
    # Arrange
    # Act
    result = get_list()
    # Assert
    assert isinstance(result, list), "Variable is not a list"

## Ensures the list is empty after reset
def test_reset_list():
    # Arrange
    reset_list()
    # Act
    result = get_list()
    # Assert
    assert len(result) == 0, "Length of list was not 0"
    
## Ensures items are correctly added to the list
def test_add_to_list():
    # Arrange
    reset_list()
    add_to_list("12345")
    add_to_list("23456")
    add_to_list("34567")
    # Act
    result = get_list()
    # Assert
    assert len(result) == 3, "The list was not 3 items long."
    assert result == ["12345","23456","34567"], "The list does not have the correct items in the correct order."

    
## Allows you to remove an item from the list 
def test_remove_from_list():
    # Arrange    
    reset_list()
    add_to_list("12345")
    # Act
    remove_from_list("12345")
    result = get_list()
    # Assert
    assert len(result) == 0, "Item was not removed from the list"  
    
## Tests raising a value error when the item to remove is not found in the list
def test_remove_from_list_missing_value():
    # Arrange    
    reset_list()
    add_to_list("12345")
    # Act
    # Assert
    with pytest.raises(ValueError):
        remove_from_list("23456")


## Tests replacing an item in the list successfully         
def test_replace_item():
    # Arrange    
    reset_list()
    add_to_list("12345")
    add_to_list("23456")
    add_to_list("34567")
    # Act
    replace_item_in_list("12345", "00000")
    replace_item_in_list("23456", "11111")
    replace_item_in_list("34567", "22222")
    result = get_list()
    # Assert
    assert len(result) == 3, "Result length was not 3"
    assert result == ["00000","11111","22222"], "Items were not replaced as expected."
    
    
## Tests raising a value error when the item to replace is not found
def test_replace_item_missing_value():
    # Arrange    
    reset_list()
    add_to_list("12345")
    # Act
    # Assert
    with pytest.raises(ValueError):
        replace_item_in_list("23456", "34567")

## Tests getting the item at the first position in the list. This is 1-based instead of 0-based
def test_get_item_at_position():
    # Arrange    
    reset_list()
    add_to_list("12345")
    # Act
    result = get_item_at_position(1)
    # Assert
    assert result == "12345", "Result was not 12345 as expected."
    
## Tests getting the item at a given position in the list. This is 1-based instead of 0-based
def test_get_item_at_position_5():
    # Arrange    
    reset_list()
    add_to_list("12345")
    add_to_list("23456")
    add_to_list("34567")
    add_to_list("45678")
    add_to_list("56789")
    # Act
    result = get_item_at_position(5)
    # Assert
    assert result == "56789", "Result was not 56789 as expected."

## Tests raising a value error when a bad position is indicated
def test_get_item_at_bad_position():
    # Arrange    
    reset_list()
    add_to_list("12345")
    add_to_list("23456")
    add_to_list("34567")
    add_to_list("45678")
    add_to_list("56789")
    # Act    
    # Assert
    with pytest.raises(ValueError):
        result = get_item_at_position(-1)
        result = get_item_at_position(0)    
        result = get_item_at_position(6)

if __name__ == '__main__':
    pytest.main([__file__])