# Write your MySQL query statement below

SELECT p.firstName, p.lastName, a.city, a.state FROM Person as p left join Address as a on p.personID = a.personID;

