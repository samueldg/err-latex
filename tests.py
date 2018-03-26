"""Basic output validation tests"""

import latex


# pytest
extra_plugin_dir = '.'
pytest_plugins = ['errbot.backends.test']



def test_with_no_arguments(testbot):
    testbot.push_message('!latex')
    result = testbot.pop_message()
    assert result == 'You need to provide a LaTeX expression to convert!'


def test_with_latex_expression(testbot):
    expression = '$E=mc^2$'
    testbot.push_message('!latex ' + expression)
    image_url = testbot.pop_message()
    assert image_url == 'http://latex.codecogs.com/png.latex?%24E%3Dmc%5E2%24'
