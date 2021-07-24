import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def searchjobs(term):

    url_sof = "https://stackoverflow.com"
    url_wwr = "https://weworkremotely.com"
    url_ro = "https://remoteok.io"

    urls = [f"{url_sof}/jobs?r=true&q={term}",
            f"{url_wwr}/remote-jobs/search?term={term}",
            f"{url_ro}/remote-dev+{term}-jobs"]

    joblist = []

    for url in urls:
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html)
        
        if url_sof in url:
            dflexs = soup.find("div", {"class": "listResults"}).find_all(
                "div", {"class": "d-flex"})
            for dflex in dflexs:
                try:
                    slink = dflex.find(
                        "a", {"class": "s-link stretched-link"})
                    title = slink.text
                    href = url_sof + slink.get("href")
                    company = dflex.find(
                        "h3", {"class": "fc-black-700 fs-body1 mb4"}).find("span").text.rstrip("\n ")
                    joblist.append(
                        {"title": title, "href": href, "company": company})
                except:
                    pass

        # elif url_wwr in url:
            
        #     jobs = soup.find_all("section", {"class": "jobs"})
        #     for job in jobs:
        #         lis = job.find_all(
        #             "li")
        #         for li in lis:
        #             try:
        #                 a = li.find_all(
        #                     "a")[1]
        #                 href = url_wwr + a.get("href")
        #                 company = a.find(
        #                     "span", {"class": "company"}).text
        #                 title = a.find(
        #                     "span", {"class": "title"}).text
        #                 joblist.append(
        #                     {"title": title, "href": href, "company": company})
        #             except:
        #                 pass

        # elif url_ro in url:
        #     tbodys = soup.find("div", {"class", "container"}).find_all("tbody")
        #     for tbody in tbodys:

        #         trs = tbody.find_all("tr")
        #         for tr in trs:
        #             try:
        #                 preventLink = tr.find_all(
        #                     "a", {"class", "preventLink"})
        #                 company = preventLink[1].text
        #                 title = preventLink[2].text
        #                 href = preventLink[2].get("href")
        #                 joblist.append(
        #                     {"title": title, "href": href, "company": company})
        #             except:
        #                 pass

    return joblist