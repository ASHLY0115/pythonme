info={}
info["name"] = "sandy"
info["occupation"] = "worker"
print(info)
thekeys = list(info.keys())
thekeys.sort()
for key in thekeys:
    print(key,info[key])