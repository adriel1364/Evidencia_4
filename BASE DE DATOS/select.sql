USE Cafebar;
SELECT * FROM Cafetera;
SELECT * FROM Cafetera WHERE capacidad > 5;
SELECT * FROM Cafetera WHERE nivel_agua < 500;
SELECT * FROM historialpreparacion WHERE cantidad >= 5;
SELECT historialpreparacion.fecha_preparacion FROM historialpreparacion ORDER BY fecha_preparacion ASC
