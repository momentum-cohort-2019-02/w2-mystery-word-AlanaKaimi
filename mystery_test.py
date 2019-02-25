from mystery_word import play_game

def test_display_word():
    word = "racecar"
    assert display_word(word, []) == "_ _ _ _ _ _ _"
    assert display_word(word, ["r"]) == "r _ _ _ _ _ r"
    assert display_word(word, ["r", "c"]) == "r _ c _ c _ r"
    assert not display_word(word, ["z"]) == "_ _ _ _ _ _ _"