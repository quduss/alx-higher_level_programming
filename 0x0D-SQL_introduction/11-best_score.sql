-- list records with score greater than or equals to 10
-- lists only the score and name fields
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
