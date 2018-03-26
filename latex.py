"""Bot that converts LaTeX expressions to images.
"""

import urllib.parse

from errbot import botcmd
from errbot import BotPlugin


class LatexBot(BotPlugin):

    api_url_template = 'http://latex.codecogs.com/svg.latex?{query}'

    @botcmd
    def latex(self, msg, args):
        """Return a card with the rendered LaTeX expression as an SVG.
        """

        if not args:
            # Get random definitions if no term is provided
            return 'You need to provide a LaTeX expression to convert!'

        else:
            expression = ' '.join(args)
            image_url = self.get_image_url(expression)
            self.send_card(in_reply_to=msg, image=image_url)

    @classmethod
    def get_image_url(cls, latex_expression):
        """Given the LaTeX expression, return the URL of the image (SVG).
        """
        escaped_expression = urllib.parse.quote(latex_expression)
        return cls.api_url_template.format(query=escaped_expression)
