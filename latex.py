"""Bot that converts LaTeX expressions to images.
"""

import urllib.parse

from errbot import botcmd
from errbot import BotPlugin


class LatexBot(BotPlugin):

    api_url_template = 'https://latex.codecogs.com/png.latex?{query}'

    @botcmd
    def latex(self, msg, args):
        """Return a card with the rendered LaTeX expression as a PNG.
        """

        if not args:
            # Get random definitions if no term is provided
            return 'You need to provide a LaTeX expression to convert!'

        else:
            image_url = self.get_image_url(args)
            self.send_card(
                image=image_url,
                in_reply_to=msg,
            )

    @classmethod
    def get_image_url(cls, latex_expression):
        """Given the LaTeX expression, return the URL of the image (PNG).
        """
        escaped_expression = urllib.parse.quote(latex_expression)
        return cls.api_url_template.format(query=escaped_expression)
