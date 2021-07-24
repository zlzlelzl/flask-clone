def write_file(term, joblist):
    with open(term+".csv", "w", encoding="utf8") as f:
        f.writerow("Title,Company,Link")
        for j in joblist:
            f.writerow(f"{j.title},{j.company},{j.link}")