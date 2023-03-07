import unittest
from main import format_reply


class TestReplyFormatting(unittest.TestCase):

    def test_format_reply(self):
        reply = "Here is some ```python\ncode``` for you to look at."
        expected_reply = 'Here is some <pre><code class="python">python\ncode</code></pre> for you to look at.'

        # Apply the formatting to the reply
        formatted_reply = format_reply(reply)

        # Check that the formatted reply matches the expected output
        self.assertEqual(formatted_reply, expected_reply)

    def test_no_code_block(self):
        reply = "This is just some regular text."

        # Apply the formatting to the reply
        formatted_reply = format_reply(reply)

        # Check that the formatted reply is the same as the input (no changes made)
        self.assertEqual(formatted_reply, reply)
