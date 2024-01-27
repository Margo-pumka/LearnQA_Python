class TestHw10:
    def test_length_of_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) != 0, "Phrase not entered"
        assert len(phrase) < 15, f"Phrase longer than 15 characters. Phrase length {len(phrase)} characters."
