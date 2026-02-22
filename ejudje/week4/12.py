import json

def isJson(val):
    return type(val) is dict

def findDiff(a, b, path=""):
    diffs = []

    if isJson(a) and isJson(b):
        keys = set(a.keys()) | set(b.keys())

        for k in keys:
            new_path = k if path == "" else path + "." + k

            if k not in a:
                diffs.append(f"{new_path} : <missing> -> {json.dumps(b[k], separators=(',', ':'), sort_keys=True)}")
            elif k not in b:
                diffs.append(f"{new_path} : {json.dumps(a[k], separators=(',', ':'), sort_keys=True)} -> <missing>")
            else:
                diffs += findDiff(a[k], b[k], new_path)

        return diffs

    if a != b:
        diffs.append(f"{path} : {json.dumps(a, separators=(',', ':'),
                                             sort_keys=True)} -> {json.dumps(b, separators=(',', ':'), sort_keys=True)}")
    return diffs


def main():
    obj1 = json.loads(input())
    obj2 = json.loads(input())

    result = findDiff(obj1, obj2)

    if not result:
        print("No differences")
    else:
        for line in sorted(result):
            print(line)


main()