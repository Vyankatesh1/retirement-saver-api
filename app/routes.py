from fastapi import APIRouter
from app.logic import parse_txns, apply_rules, calc_returns

router = APIRouter()

@router.post("/api/v1/transactions/parse")
def parse_transactions(data: list):
    return parse_txns(data)

@router.post("/api/v1/transactions/filter")
def filter_transactions(body: dict):
    return apply_rules(body)

@router.post("/api/v1/returns/index")
def index_returns(body: dict):
    return calc_returns(body)