import json

def isJson(val):
    if type(val) is dict:
        return True
    return False

def applyPatch(source, patch):
    for k in patch.keys():
        if patch.get(k) is None:
            source.pop(k)
        elif isJson(source.get(k)) and isJson(patch.get(k)):
            applyPatch(source[k], patch[k])
        else:
            source[k] = patch[k]
    return source

def test1():
    source =json.loads("{\"user\":{\"name\":\"Ann\",\"age\":20},\"active\":true}")
    patch = json.loads("{\"user\":{\"age\":21},\"active\":false}")
    result = applyPatch(source, patch)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))    

def main():
    result = applyPatch(json.loads(input()), json.loads(input()))
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))

main()