with dummy as (
    select
        1 as id,
        'test' as nama
)
select
    id,
    nama
from dummy