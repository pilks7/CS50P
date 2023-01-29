from seasons import minutes_born, nums_to_words
import pytest


def test_nums_to_words():
    assert nums_to_words(1234567) == "One million, two hundred thirty-four thousand, five hundred sixty-seven minutes"


