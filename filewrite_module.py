def write_file(term, joblist):
    with open(term + ".csv", "w", encoding="utf8") as f:
        f.write("Title,Company,Link\n")
        for j in joblist:
            f.write(f"\"{j['title']}\",\"{j['company']}\",\"{j['link']}\"\n")
