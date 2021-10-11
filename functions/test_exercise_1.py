import textwrap

from exercise_1 import reverse_text, upper_text


def test_reverse_text():
    text = reverse_text()

    assert text == textwrap.dedent(
        """
        .meht dnib ssenkrad eht ni dna
        ,lla meht gnirb ot gniR enO
        ,meht dnif ot gniR enO
        ,lla meht elur ot gniR enO"""
    )


def test_upper_text():
    text = upper_text()

    assert text == textwrap.dedent(
        """\
        ONE RING TO RULE THEM ALL,
        ONE RING TO FIND THEM,
        ONE RING TO BRING THEM ALL,
        AND IN THE DARKNESS BIND THEM.
        """
    )
