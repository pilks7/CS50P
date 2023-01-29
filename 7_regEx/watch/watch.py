import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    if matches := re.match(r".*src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)", s, re.IGNORECASE):
        match = matches.group(1)
        return f"https://youtu.be/{match}"
    else:
        return None




if __name__ == "__main__":
    main()


    #src="http://www.youtube.com/embed/xvFZjo5PgG0" converting them back to   https://youtu.be/xvFZjo5PgG0