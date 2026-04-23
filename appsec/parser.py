
def parse_log(file):
    log = []

    with open(file, "r") as f:
        for line in f:
            print(line)
            log.append(line)

        return log
    
# print(parse_log("/var/log/auth.log"))