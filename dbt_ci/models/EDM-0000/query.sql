with dummy as (
    select
        1 as id,
        'test1' as nama,
        'EDM-0000' flag
)
select
    id,
    nama,
    flag
from dummy