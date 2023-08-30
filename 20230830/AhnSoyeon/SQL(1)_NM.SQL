select a.animal_id, a.tmpName as "NAME", a.sex_upon_intake
from (SELECT animal_id, 
         case name 
        when "Lucy" then name
        when "Ella" then name
        when "Pickle" then name
        when "Rogan" then name
        when "Sabrina" then name
        when "Mitty" then name
        end as "tmpName"
        , sex_upon_intake
from animal_ins
) as a 
where a.tmpName is not null
order by 1
