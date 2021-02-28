--select p.state ,count(*) from person p
--group by p.state 

--select p.first_name ,p2.first_name ,p.zip
--from person p inner join person p2 
--on p.zip = p2.zip 
--where p2.person_id != p.person_id 

SELECT zip, string_agg(first_name , ', ') FROM person p2 GROUP BY zip;

--select p2.last_name from person p2 where p2.last_name like ('s%')
    