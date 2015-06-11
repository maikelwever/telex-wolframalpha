from telex import plugin
from urllib.parse import quote
import wolframalpha


class WolframAlphaPlugin(plugin.TelexPlugin):
    """
    WolframAlpha plugin for Telex bot.
    """

    patterns = {
        "^!wolfram (.+)$": "wolfram"
    }

    usage = [
        "!wolfram <question>"
    ]

    config_options = {
        "api_key": "API key for Wolfram API"
    }

    def wolfram(self, msg, matches):
        question = matches.group(1)
        client = wolframalpha.Client(self.read_option('api_key'))
        res = client.query(question)
        try:
            result_text = next(res.results).text
        except StopIteration:
            if not len(res.pods):
                result_text = "No results :("
            else:
                result_text = "\n".join("* {0}:\n    - {1}".format(i.title, "\n    - ".join(i.text.split("\n")))
                                        for i in res.pods if i.text)

        result_text += "\nPowered by http://wolframalpha.com/input/?i=" + quote(question, safe='')
        return result_text
