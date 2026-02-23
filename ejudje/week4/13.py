import json

def resolve_query(data, query):
    i = 0
    cur = data

    while i < len(query):
        key = ""
        while i < len(query) and query[i] not in ".[":
            key += query[i]
            i += 1

        if key:
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                return "NOT_FOUND"

        if i < len(query) and query[i] == "[":
            i += 1
            index = ""
            while i < len(query) and query[i] != "]":
                index += query[i]
                i += 1
            i += 1

            if isinstance(cur, list) and index.isdigit():
                idx = int(index)
                if 0 <= idx < len(cur):
                    cur = cur[idx]
                else:
                    return "NOT_FOUND"
            else:
                return "NOT_FOUND"

        if i < len(query) and query[i] == ".":
            i += 1

    return json.dumps(cur, separators=(",", ":"))

data = json.loads(input())
q = int(input())

for _ in range(q):
    print(resolve_query(data, input().strip()))