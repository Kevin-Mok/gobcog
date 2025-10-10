import json, random, math, sys
PATH = "/home/kevin/coding/gobcog/adventure/data/default/monsters.json"  # <-- put your path here

with open(PATH) as f:
    data = json.load(f)
assert isinstance(data, dict), "Expected dict-of-monsters JSON"

names = sorted(data.keys())
# Eligible = not a boss and not already gated by a non-members requirement
candidates = []
for n in names:
    m = data[n]
    if m.get("boss"):
        continue
    req = (m.get("miniboss") or {}).get("requirements")
    if isinstance(req, list) and req and req[0] != "members":
        # e.g. ["item", "shiny"] — keep as-is
        continue
    candidates.append(n)

random.seed(1337)                 # deterministic selection
random.shuffle(candidates)
three_count = max(1, round(len(candidates) * 0.20))
three_set = set(candidates[:three_count])  # ~20% => 3-player

for n in names:
    m = data[n]
    hp = m.get("hp")
    # 3-player gated monsters
    if n in three_set:
        mb = m.setdefault("miniboss", {})
        if not isinstance(mb.get("requirements"), list) or (mb["requirements"] and mb["requirements"][0] == "members"):
            mb["requirements"] = ["members", 3]  # gate to 3+ players
        if isinstance(hp, (int, float)):
            m["hp"] = max(10, round(hp * 0.90))
        for k, sf in (("pdef", 0.90), ("mdef", 0.90)):
            if isinstance(m.get(k), (int, float)):
                m[k] = max(0, round(m[k] * sf, 2))
    # 2-player friendly monsters
    else:
        if isinstance(hp, (int, float)):
            m["hp"] = max(10, round(hp * 0.70))
        for k, sf in (("pdef", 0.85), ("mdef", 0.85)):
            if isinstance(m.get(k), (int, float)):
                m[k] = max(0, round(m[k] * sf, 2))

with open(PATH, "w") as f:
    json.dump(data, f, indent=2)
print("Done. ~20% of non-boss monsters now require members >= 3 and stats scaled for 2p.")
