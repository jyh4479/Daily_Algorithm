SELECT NAME, COUNT(NAME) as COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING NAME IS NOT NULL and COUNT(NAME)>=2
ORDER BY NAME