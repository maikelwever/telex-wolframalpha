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
        client = wolframalpha.Client(self.read_config('api_key'))
        res = client.query(question)
        result_text = "\n".join(next(res.results).text)
        result_text += "\nPowered by https://wolframalpha.com/input/?i=" + quote(question, safe='')
        return result_text
