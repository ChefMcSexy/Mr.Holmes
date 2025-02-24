# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import requests
import json
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename


class Search:

    @staticmethod
    def search(error, report, site1, site2, http_proxy, sites, data1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        searcher = requests.get(
            url=site2, headers=headers, proxies=http_proxy, timeout=10, allow_redirects=True)
        f = open(report, "a")
        if error == "Status-Code":
            if searcher.status_code == 200:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "Found", "None").format(subject, username))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                if Writable == True:
                    f.write(site1 + "\r\n")
                else:
                    f.write("{}:{}\r\n".format(name, main))
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)
            elif searcher.status_code == 404 or searcher.status_code == 204:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "NotFound", "None").format(subject, username))
            else:
                print(Font.Color.BLUE + "[N]" +
                      Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
        elif error == "Message":
            text = sites[data1]["text"]
            if text in searcher.text:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "NotFound", "None").format(subject, username))
            else:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "Found", "None").format(subject, username))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                if Writable == True:
                    f.write(site1 + "\r\n")
                else:
                    f.write("{}:{}\r\n".format(name, main))
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)

        elif error == "Response-Url":
            response = sites[data1]["response"]
            if searcher.url == response:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "NotFound", "None").format(subject, username))
            else:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "Found", "None").format(subject, username))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                if Writable == True:
                    f.write(site1 + "\r\n")
                else:
                    f.write("{}:{}\r\n".format(name, main))
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)

        d = open(json_file2, "w")
        d.write('''{
                    "Names":[

                    ]
                }''')
        d.close()

        f = open(json_file, "w")
        f.write('''{
                    "List":[

                    ]
                }''')
        f.close()

        for element in successfullName:
            data = {
                "name": "{}".format(element)
            }
            with open(json_file2, 'r+') as file2:
                file_data2 = json.load(file2)
                file_data2["Names"].append(data)
                file2.seek(0)
                json.dump(file_data2, file2, indent=4)

        for element in successfull:
            data = {
                "site": "{}".format(element)
            }
            with open(json_file, 'r+') as file:
                file_data = json.load(file)
                file_data["List"].append(data)
                file.seek(0)
                json.dump(file_data, file, indent=4)
