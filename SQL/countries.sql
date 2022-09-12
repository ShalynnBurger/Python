
-- Question 1
-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- LEFT JOIN languages ON countries.id = languages.country_id
-- WHERE language = 'Slovene'
-- ORDER BY languages.percentage DESC;

-- Question 2
-- SELECT countries.name, count(*) as cities
-- FROM cities
-- LEFT JOIN countries on cities.country_code = countries.code
-- GROUP BY countries.name
-- ORDER BY cities DESC;

-- Question 3
-- SELECT name, population, country_id
-- FROM cities
-- WHERE country_id = 136 and population > 500000
-- ORDER BY population DESC;

-- Question 4
-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- LEFT JOIN languages ON countries.id = languages.country_id
-- WHERE percentage > 89.0
-- ORDER BY languages.percentage DESC;

-- Question 5
-- SELECT name, surface_area, population
-- FROM countries
-- WHERE surface_area<501 AND population>100000;

-- Question 6
-- SELECT name, government_form, capital, life_expectancy
-- FROM countries
-- WHERE capital>200 AND life_expectancy>75 AND government_form = 'Constitutional Monarchy';

-- Question 7
-- SELECT countries.name, cities.name, cities.district, cities.population
-- FROM countries
-- LEFT JOIN cities ON countries.id = cities.country_id
-- WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population >500000;

-- Question 8
-- SELECT region, COUNT(id) AS number_countries
-- FROM countries
-- GROUP BY region 
-- ORDER BY COUNT(id) DESC;