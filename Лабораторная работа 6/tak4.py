import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename, "r") as f:
        header = f.readline().rstrip(new_line).split(delimiter)
        spisok = []
        telo = f.readlines()
        for i in range(len(telo)):
            telo_1 = telo[i].rstrip(new_line).split(delimiter)
            spisok.append({header[i]: telo_1[i] for i in range(len(header))})
        return (spisok)


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
