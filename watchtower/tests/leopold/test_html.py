from selectolax.parser import HTMLParser

from watchtower.leopold import html


def test_to_html(email_content):
    email_html = email_content.read()
    html_content = html.to_html(email_html)
    assert html_content.html == HTMLParser(email_html).html


def test_get_sold_out(leopold_sold_out_html):
    span = html.get_sold_out(leopold_sold_out_html)
    assert span.text() == "품절"


def test_if_in_stock_then_node_is_none(leopold_in_stock_html):
    node = html.get_sold_out(leopold_in_stock_html)
    assert node is None
