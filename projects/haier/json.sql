-- json
select debit_id, paramter
from meihao_self_credit_request
where request_type = 'acard'
order by create_time desc
limit 100

/* 全数值格式
'td_6m_apply_p2p_cnt',
'td_idcard_3m_contact_phone_cnt',
'consumer_apply_amount',
'td_3m_apply_bank_xiaojin_cnt',
'td_idcard_middle_risk_list',
'alipay_credit_score',
'td_6m_apply_m_xiaojin_cnt',
'td_6m_apply_microloan_cnt',
'month_count',
'final_score',
'td_idcard_low_risk_list',
'bj_score',
'age'
*/