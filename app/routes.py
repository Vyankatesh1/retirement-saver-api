from fastapi import APIRouter
router = APIRouter()
@router.post("/api/v1/transactions/parse")
def parse_transactions(payload: dict):
    raw_text = payload.get("raw_text", "")

    if not raw_text:
        return {"error": "raw_text is required"}

    words = raw_text.split()

    merchant = words[0] if len(words) > 0 else ""
    amount = 0
    date = ""

    for w in words:
        if w.isdigit():
            amount = int(w)
        if "-" in w and len(w) == 10:
            date = w

    return {
        "merchant": merchant,
        "amount": amount,
        "date": date
    }