-- json
select debit_id, paramter
from meihao_self_credit_request
where request_type = 'acard'
order by create_time desc
limit 100