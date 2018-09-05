-- 1
-- SELECT project_id
--     FROM project_uses_tech
--         WHERE tech_id = 3;
-- 2
-- SELECT project.name from project_uses_tech
--     JOIN project ON project_uses_tech.project_id = 4
--     JOIN tech ON project_uses_tech.tech_id = tech.id;
-- 3
-- SELECT tech.name from tech
--     left outer join project_uses_tech ON tech.id = tech_id WHERE project_id  is NULL ;
-- 4
-- SELECT project.name, COUNT(*) from project_uses_tech 
--     JOIN project ON project.id = project_id GROUP BY project.name;
-- 5
-- SELECT project.name from project
--     left outer join project_uses_tech ON project.id = project_id WHERE project_id  is NULL;
-- 6
-- SELECT tech.name, COUNT(*) from project_uses_tech 
--     JOIN tech ON tech.id = tech_id GROUP BY tech.name;
-- 7
-- SELECT project.name, tech.name from project
--     full outer JOIN project_uses_tech ON project_uses_tech.project_id = project.id
--     left JOIN tech ON project_uses_tech.tech_id = tech.id;
-- 8
-- SELECT distinct(tech.name) from tech
--     JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id
--      JOIN project ON project_uses_tech.project_id = project.id;
-- 9
-- SELECT tech.name from tech
--     full outer JOIN project_uses_tech ON project_uses_tech.tech_id = tech.id WHERE project_id is NULL;
-- 10
-- SELECT distinct(project.name) from project
--     JOIN project_uses_tech ON project_uses_tech.project_id = project.id
--      JOIN tech ON project_uses_tech.tech_id = tech.id;
-- 11
-- SELECT project.name from project
--     full outer JOIN project_uses_tech ON project_uses_tech.project_id = project.id WHERE tech_id is NULL;
-- 12
-- SELECT project.name, COUNT(*) from project_uses_tech 
--     full outer JOIN project ON project.id = project_id WHERE tech_id>0 GROUP BY project.name ORDER BY count DESC  ;
-- 13
-- SELECT tech.name, COUNT(*) from project_uses_tech 
--     full outer JOIN tech ON tech.id = tech_id GROUP BY tech.name ORDER BY count DESC;
-- 14
-- SELECT AVG(councode ex1.sql