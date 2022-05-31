SELECT m.dataset_id, m."key", m.value,
d.kode_skpd, d."name", d.title,d.description, d."schema", d."table",d.category
FROM public.metadata as m
join public.dataset d
on d.id = m.dataset_id
where lower(m.key) = 'pengukuran dataset' or lower(m.key) = 'tingkat penyajian dataset' or lower(m.key) = 'cakupan dataset'
order by dataset_id ;