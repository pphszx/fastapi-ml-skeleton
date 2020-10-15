from typing import List
from pydantic import BaseModel


class HaierPredictionPayload(BaseModel):
    td_6m_apply_p2p_cnt: int
    td_idcard_3m_contact_phone_cnt: int
    consumer_apply_amount: int
    td_3m_apply_bank_xiaojin_cnt: int
    td_idcard_middle_risk_list: int
    alipay_credit_score: int
    td_6m_apply_m_xiaojin_cnt: int
    td_6m_apply_microloan_cnt: int
    month_count: int
    final_score: int
    td_idcard_low_risk_list: int
    bj_score: int
    age: int


class HaierPredictionResult(BaseModel):
    good_prob: float
    bad_prob: float


def payload_to_list(HPP: HaierPredictionPayload) -> List:
    return [
        HPP.td_6m_apply_p2p_cnt,
        HPP.td_idcard_3m_contact_phone_cnt,
        HPP.consumer_apply_amount,
        HPP.td_3m_apply_bank_xiaojin_cnt,
        HPP.td_idcard_middle_risk_list,
        HPP.alipay_credit_score,
        HPP.td_6m_apply_m_xiaojin_cnt,
        HPP.td_6m_apply_microloan_cnt,
        HPP.month_count,
        HPP.final_score,
        HPP.td_idcard_low_risk_list,
        HPP.bj_score,
        HPP.age,
    ]
