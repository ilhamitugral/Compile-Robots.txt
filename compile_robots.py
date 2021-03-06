"""

Robots.txt Compiler
@author: Ilhami TUGRAL <ilhamitugral@gmail.com>
@date: 11/2/20

"""

import requests
import sys

def drawError(value):
    print("\n{0}\n".format(value))

def ReadRobots(address):
    # We're sending request.
    rq = requests.get(address + '/robots.txt')

    # If target website is reachable, we can start to operations.
    if rq.status_code == 200:
        robots = ["*"]

        rule = False  # We can control robots with this variable.
        sitemaps = []  # All sitemaps is here.
        blacklist = []  # All Disallowed pages here.
        whitelist = []  # All Allowed pages is here.

        # Content is binary code. We need convert to UTF-8 or ASCII
        # And we are catching every lines.
        data = rq.content.decode('utf-8').split("\n")

        for i in data:
            if not i.startswith('#') and not i == "":
                info = i.split(':')

                # We're changing ' :' to ':'
                info[1] = info[1].replace(' ', '')

                # If parameter is User-agent, we are changing rule.
                if info[0] == 'User-agent':
                    if info[1] in robots:
                        rule = True

                # If parameter is Disallow, we are adding to blacklist list.
                if info[0] == 'Disallow' and rule:
                    if not info[1] in blacklist:
                        blacklist.append(info[1])

                # If parameter is Allow, we are adding to whitelist list.
                if info[0] == 'Allow' and rule:
                    if not info[1] in whitelist:
                        whitelist.append(info[1])

                # We are adding every Sitemap parameter to sitemaps list.
                if info[0] == 'Sitemap':
                    sitemaps.append(info[1] + ':' + info[2])  # We are re-formatting split format again.

        # Let's return all information's back.
        return {
            'status': 'success',
            'sitemap': sitemaps,
            'blacklist': blacklist,
            'whitelist': whitelist
        }
    else:
        # If website is unreachable; We are returning error information's.
        return {
            'status': 'error',
            'message': 'Robots.txt unreachable: ' + str(rq.status_code),
        }

if len(sys.argv) > 1:
    # Target website
    if isinstance(sys.argv[1], str):
        site = sys.argv[1]

        if(sys.argv[1].startswith("http")):
            # We're converting https://example.com/ to https://example.com
            if site.endswith('/'):
                site = site[0:len(site) - 1]

            # We are sending request root website
            r = requests.get(site)

            # If website is reachable, we can start to operations.
            if r.status_code == 200:

                # Let's compile here.
                robotsData = ReadRobots(site)

                # And let's check.
                if robotsData['status'] == 'success':
                    print(robotsData)
                else:
                    print(robotsData['message'])

            else:
                # Let's print website is unreachable error.
                drawError('Connection Error: ' + str(r.status_code))
        elif sys.argv[1] == "-h":
            # Let's show example using
            drawError("Example use: \"compile_robots.py [https://example.com]\"")
        else:
            # If format is wrong: lets print errpr
            drawError("Error: Website invalid.")
    else:
        # If data is not string:
        drawError("Error: Invalid value.")
else:
    # Let's show example using
    drawError("Error: You need to add website. Help: \"compile_robots.py -h\"")
