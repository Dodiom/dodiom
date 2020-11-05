import csv

with open("translation.csv", "r", encoding="utf8") as translation_csv:
    reader = csv.DictReader(translation_csv)
    csv_lines = []
    for row in reader:
        csv_lines.append([row["Token name"],
                          row["English"].replace("\"", "\\\"").replace("\'", "\\\'").strip(),
                          row["Turkish"].replace("\"", "\\\"").replace("\'", "\\\'").strip(),
                          row["Italian"].replace("\"", "\\\"").replace("\'", "\\\'").strip()
                          ])

    # print enum class
    print("class Token(Enum):")
    for line in csv_lines:
        print(f"    {line[0]} = auto()")

    # print translations
    print("\n\ntranslations = {")
    for line in csv_lines:
        if line[0] != "HELP_MESSAGE":
            print(f"    Token.{line[0]}: {{")
            print(f"        \"en\": \"{line[1]}\",")
            print(f"        \"tr\": \"{line[2]}\",")
            print(f"        \"it\": \"{line[3]}\"")
            print(f"    }},")
        else:
            print(f"    Token.{line[0]}: {{")
            print(f"        \"en\": \"\"\"\n{line[1]}\n\"\"\",")
            print(f"        \"tr\": \"\"\"\n{line[2]}\n\"\"\",")
            print(f"        \"it\": \"\"\"\n{line[3]}\n\"\"\"")
            print(f"    }},")
    print("}")
