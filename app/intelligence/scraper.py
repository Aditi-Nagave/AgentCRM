# app/intelligence/scraper.py

import requests

from bs4 import BeautifulSoup

from app.intelligence.robots_checker import (
    robots_allowed
)

def scrape_website(url):

    try:

        if not robots_allowed(url):

            return {

                "status":"blocked",

                "reason":"robots.txt"
            }

        response = requests.get(

            url,

            headers={

                "User-Agent":
                "Mozilla/5.0"
            },

            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.text \
            if soup.title \
            else "No Title"

        paragraphs = []

        for p in soup.find_all("p")[:20]:

            text = p.get_text(
                strip=True
            )

            if text:

                paragraphs.append(
                    text
                )

        return {

            "status":"success",

            "title":title,

            "content":
            paragraphs
        }

    except Exception as e:

        return {

            "status":"failed",

            "error":str(e)
        }