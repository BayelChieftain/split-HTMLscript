import unittest
from msg_split import split_message

class TestSplitMessage(unittest.TestCase):
    def test_split_message(self):
        source = """<p>Some text <b>with bold</b> and normal text.</p><p>Another paragraph.</p>"""
        fragments = list(split_message(source, max_len=50))
        self.assertEqual(len(fragments), 2)
        self.assertTrue(all(len(fragment) <= 50 for fragment in fragments))

    def test_split_message_with_long_text(self):
        source = "<p>" + "a" * 5000 + "</p>"
        with self.assertRaises(Exception):
            list(split_message(source, max_len=4096))

if __name__ == "__main__":
    unittest.main()


