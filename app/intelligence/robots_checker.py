# app/intelligence/robots_checker.py
import requests
from urllib.parse import urlparse


def robots_allowed(url):

    try:

        parsed = urlparse(url)

        robots_url = (
            f"{parsed.scheme}://"
            f"{parsed.netloc}/robots.txt"
        )

        response = requests.get(
            robots_url,
            timeout=5
        )

        if response.status_code != 200:
            return False

        content = response.text.lower()

        return "disallow: /" not in content

    except:

        return False