from unittest import TestCase

from btoa import btoa, atob


class MainCase(TestCase):
    def test_btoa(self):
        self.assertEqual(
            btoa("Hello World"),
            "SGVsbG8gV29ybGQ="
        )
        self.assertEqual(
            btoa('s8ë{LóüÈ@É"¹ÏLôa"¢f#½2r[¢ÀCwÀ¯ÅaõdUí£tùºm94±]!'),
            "czjre0zz/MhAySK5z0z0YSKiZiO9MnJbosBDd8CvxWH1ZFXto3T5um05NLFdIQ=="
        )

    def test_atob(self):
        self.assertEqual(
            atob("SGVsbG8gV29ybGQ="),
            "Hello World"
        )
        self.assertEqual(
            atob("czjre0zz/MhAySK5z0z0YSKiZiO9MnJbosBDd8CvxWH1ZFXto3T5um05NLFdIQ=="),
            's8ë{LóüÈ@É"¹ÏLôa"¢f#½2r[¢ÀCwÀ¯ÅaõdUí£tùºm94±]!'
        )
