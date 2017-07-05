SELECT country_code, language, percentage
FROM languages
WHERE language = "slovene"
ORDER BY percentage DESC;

SELECT countries.name, COUNT(cities.name) AS city_count
FROM cities
JOIN countries ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.name) DESC;
 
SELECT * FROM cities
WHERE country_code = "MEX" and population > 500000
ORDER BY population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM languages
JOIN countries ON countries.id = languages.country_id
WHERE percentage > 89
ORDER BY languages.percentage DESC;

SELECT  countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

SELECT countries.name, countries.government_form, countries.capital 
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy'
AND countries.life_expectancy > 75
AND countries.capital > 200;

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
	JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
	AND cities.district = 'Buenos Aires'
	AND cities.population > 500000;

SELECT countries.region, COUNT(countries.id) AS num_countries
FROM countries
GROUP BY countries.region
ORDER BY num_countries DESC;






