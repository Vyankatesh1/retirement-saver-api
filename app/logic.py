from app.utils import to_dt

def parse_txns(expense_list):
    res = []
    for item in expense_list:
        amt = item["amount"]
        rounded = ((amt + 99) // 100) * 100
        saved = rounded - amt

        res.append({
            "timestamp": item["date"],
            "amount": amt,
            "rounded_amount": rounded,
            "saved": saved
        })
    return res


def apply_rules(payload):
    txns = payload.get("transactions", [])
    q_rules = payload.get("q", [])
    p_rules = payload.get("p", [])

    data = []

    for t in txns:
        dt = to_dt(t["timestamp"])
        saved = t["saved"]

        # apply q rules (override)
        chosen = None
        for q in q_rules:
            s = to_dt(q["start"])
            e = to_dt(q["end"])

            if s <= dt <= e:
                if chosen is None or s > to_dt(chosen["start"]):
                    chosen = q

        if chosen:
            saved = chosen["fixed"]

        # apply p rules (add)
        for p in p_rules:
            s = to_dt(p["start"])
            e = to_dt(p["end"])

            if s <= dt <= e:
                saved += p["extra"]

        t["saved"] = saved
        data.append(t)

    return {
        "data": data,
        "errors": []
    }


def calc_returns(body):
    age = body["age"]
    inflation = body["inflation"]
    txns = body["transactions"]
    ranges = body["k"]

    years = 60 - age if age < 60 else 5
    rate = 0.1449

    savings = []

    for r in ranges:
        s = to_dt(r["start"])
        e = to_dt(r["end"])

        total_saved = 0

        for t in txns:
            dt = to_dt(t["timestamp"])
            if s <= dt <= e:
                total_saved += t["saved"]

        gross = total_saved * ((1 + rate) ** years)
        real = gross / ((1 + inflation) ** years)

        savings.append({
            "start": r["start"],
            "end": r["end"],
            "amount": round(total_saved, 2),
            "returns": round(real, 2)
        })

    return {
        "total_amount": sum(x["amount"] for x in txns),
        "total_rounded": sum(x["rounded_amount"] for x in txns),
        "savings": savings
    }