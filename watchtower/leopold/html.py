from typing import Optional

from selectolax.parser import HTMLParser, Node


def to_html(html: str) -> HTMLParser:
    return HTMLParser(html)


def get_sold_out(html: HTMLParser) -> Optional[Node]:
    css_selector = "#formItem > table > tbody > tr:nth-child(2) > td > span"
    return html.css_first(css_selector)
