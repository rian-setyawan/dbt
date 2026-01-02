with dummy as (
    select
        2 as id,
        'test2' as nama,
        'EDM-0001' flag
)
select
    id,
    nama,
    flag
from dummy