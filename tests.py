from numtowordsuz import number_to_text


def test_num_to_text():
    assert number_to_text("11-sentabr") == "o‘n birinchi sentabr"
    assert number_to_text("2.3") == "ikki butun uch"
    assert number_to_text("2,3") == "ikki butun uch"
    assert number_to_text("-2") == "minus ikki"


if __name__ == "__main__":
    test_num_to_text()
    print("Tests passed")