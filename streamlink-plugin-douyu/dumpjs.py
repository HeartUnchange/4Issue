import re
import requests
import jsbeautifier
import sys
import typing
import datetime

DOUYU_BASE_URL = "https://www.douyu.com/{room_id}"
_url_re = re.compile(
    r"http(s)?://(?:(?P<subdomain>.+)\.)?douyu.com/(?:show/(?P<vid>[^/&?]+)|(?P<roomid>\d+))", re.VERBOSE)


def dump_js(*args):
    date = datetime.date.today().strftime("%Y%m%d")
    for arg in args:
        target = fetch_js(arg)
        filename = "%s_%s.js" % (target.get("roomid"), date)
        with open(filename, "w") as f:
            f.write(target.get("content", ""))


def fetch_js(url: str) -> typing.Dict:
    match = _url_re.match(url)
    room_id = match.group("roomid")
    if not room_id:
        return {}
    html = requests.get(DOUYU_BASE_URL.format(room_id=room_id))

    param = re.findall(r"function ub98484234\(([^,]*)", html.text)[0]
    const = re.findall(r"var %s=\[[^]]*\]" %
                       param[:len(param) - 1], html.text)[0]
    function = re.findall(
        r"function ub98484234.*return eval\(strc\)\(%s[^}]*;\}" % param, html.text)[0]
    return {"roomid": room_id, "content": jsbeautifier.beautify(";".join([const, function]))}


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 2:
        print('no enough args')
    dump_js(*args)
